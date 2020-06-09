"""
Offers a functional interface to the device functionality
"""

import asyncio
import itertools
import re
from contextlib import suppress
from functools import partialmethod
from typing import Awaitable, Callable, List, Optional, Type, Union

from aiohttp import web
from brewblox_service import brewblox_logger, features, strex

from brewblox_devcon_spark import (commander, commands, const, datastore,
                                   exceptions, twinkeydict)
from brewblox_devcon_spark.codec import codec

ObjectId_ = Union[str, int]
FindIdFunc_ = Callable[[twinkeydict.TwinKeyDict, ObjectId_, str], Awaitable[ObjectId_]]

LOGGER = brewblox_logger(__name__)


class SparkResolver():

    def __init__(self, app: web.Application):
        self._app = app
        self._datastore = datastore.get_block_store(app)
        self._codec = codec.get_codec(app)

    @staticmethod
    def _get_content_objects(content: dict) -> List[dict]:
        objects_to_process = [content]
        with suppress(KeyError):
            objects_to_process += content['objects']
        with suppress(KeyError):
            objects_to_process += content['object_ids']
        return objects_to_process

    def _assign_id(self, input_type: str):
        clean_name = re.sub(r',driven', '', input_type)
        for i in itertools.count(start=1):  # pragma: no cover
            name = f'{const.GENERATED_ID_PREFIX}{clean_name}-{i}'
            if (name, None) not in self._datastore:
                return name

    async def _process_data(self,
                            codec_func: codec.TranscodeFunc_,
                            content: dict,
                            opts: Optional[dict]
                            ) -> dict:
        objects_to_process = self._get_content_objects(content)

        for obj in objects_to_process:
            # transcode type + data
            with suppress(KeyError):
                new_type, new_data = await codec_func(
                    obj['type'],
                    obj['data'],
                    opts=opts,
                )
                obj['type'] = new_type
                obj['data'] = new_data
            # transcode interface (type only)
            with suppress(KeyError):
                new_type = await codec_func(obj['interface'], opts=opts)
                obj['interface'] = new_type

        return content

    def _find_nid(self,
                  store: twinkeydict.TwinKeyDict,
                  sid: str,
                  input_type: str,
                  ) -> int:
        if sid is None:
            return 0

        if isinstance(sid, int) or sid.isdigit():
            return int(sid)

        try:
            return store.right_key(sid)
        except KeyError:
            raise exceptions.UnknownId(f'No numeric ID matching [sid={sid},type={input_type}] found in store')

    def _find_sid(self,
                  store: twinkeydict.TwinKeyDict,
                  nid: int,
                  input_type: str,
                  ) -> str:
        if nid is None or nid == 0:
            return None

        if isinstance(nid, str):
            raise exceptions.DecodeException(f'Expected numeric ID, got string "{nid}"')

        try:
            sid = store.left_key(nid)
        except KeyError:
            # If service ID not found, randomly generate one
            sid = self._assign_id(input_type)
            store[sid, nid] = dict()

        return sid

    async def _resolve_links(self,
                             finder_func: FindIdFunc_,
                             content: dict
                             ) -> dict:
        store = self._datastore
        objects_to_process = self._get_content_objects(content)

        async def traverse(data):
            """Recursively finds and resolves links"""
            iter = enumerate(data) \
                if isinstance(data, (list, tuple)) \
                else data.items()

            for k, v in iter:
                if isinstance(v, (dict, list, tuple)):
                    await traverse(v)
                elif str(k).endswith(const.OBJECT_LINK_POSTFIX_END):
                    link_type = k[k.rfind(const.OBJECT_LINK_POSTFIX_START)+1:-1]
                    data[k] = finder_func(store, v, link_type)

        for obj in objects_to_process:
            with suppress(KeyError):
                await traverse(obj['data'])

        return content

    async def encode_data(self, content: dict, opts: Optional[dict]) -> dict:
        return await self._process_data(self._codec.encode, content, opts)

    async def decode_data(self, content: dict, opts: Optional[dict]) -> dict:
        return await self._process_data(self._codec.decode, content, opts)

    async def convert_sid_nid(self, content: dict, _=None) -> dict:
        objects_to_process = self._get_content_objects(content)

        for obj in objects_to_process:
            # Remove the sid
            sid = obj.pop('id', None)

            if sid is None or 'nid' in obj:
                continue

            obj['nid'] = self._find_nid(
                self._datastore,
                sid,
                obj.get('type') or obj.get('interface'))

        return content

    async def add_sid(self, content: dict, _=None) -> dict:
        objects_to_process = self._get_content_objects(content)

        for obj in objects_to_process:
            # Keep the nid
            nid = obj.get('nid', None)

            if nid is None:
                continue

            obj['id'] = self._find_sid(
                self._datastore,
                nid,
                obj.get('type') or obj.get('interface'))

        return content

    async def convert_links_nid(self, content: dict, _=None) -> dict:
        return await self._resolve_links(self._find_nid, content)

    async def convert_links_sid(self, content: dict, _=None) -> dict:
        return await self._resolve_links(self._find_sid, content)


class SparkController(features.ServiceFeature):

    def __init__(self, name: str, app: web.Application):
        super().__init__(app)
        self._commander: commander.SparkCommander = None

    async def startup(self, app: web.Application):
        self._commander = commander.get_commander(app)

    async def shutdown(self, _):
        pass

    async def validate(self, content_: dict = None, **kwargs) -> dict:
        content = content_ or dict()
        content.update(kwargs)
        opts = {}

        resolver = SparkResolver(self.app)

        for afunc in [
            resolver.convert_sid_nid,
            resolver.convert_links_nid,
            resolver.encode_data,
            resolver.decode_data,
            resolver.convert_links_sid,
            resolver.add_sid,
        ]:
            content = await afunc(content, opts)

        return content

    async def _execute(self,
                       command_type: Type[commands.Command],
                       command_opts: Optional[dict],
                       content_: dict = None,
                       **kwargs
                       ) -> dict:
        # Allow a combination of a dict containing arguments, and loose kwargs
        content = content_ or dict()
        content.update(kwargs)

        try:
            resolver = SparkResolver(self.app)

            # pre-processing
            for afunc in [
                resolver.convert_sid_nid,
                resolver.convert_links_nid,
                resolver.encode_data,
            ]:
                content = await afunc(content, command_opts)

            # execute
            retval = await self._commander.execute(
                command_type.from_decoded(content)
            )

            # post-processing
            for afunc in [
                resolver.decode_data,
                resolver.convert_links_sid,
                resolver.add_sid,
            ]:
                retval = await afunc(retval, command_opts)

            return retval

        except asyncio.CancelledError:  # pragma: no cover
            raise

        except Exception as ex:
            LOGGER.debug(f'Failed to execute {command_type}: {strex(ex)}')
            raise ex

    noop = partialmethod(_execute, commands.NoopCommand, None)

    read_object = partialmethod(_execute, commands.ReadObjectCommand, None)
    read_logged_object = partialmethod(_execute, commands.ReadObjectCommand, {codec.STRIP_UNLOGGED_KEY: True})
    read_stored_object = partialmethod(_execute, commands.ReadStoredObjectCommand, None)
    write_object = partialmethod(_execute, commands.WriteObjectCommand, None)
    create_object = partialmethod(_execute, commands.CreateObjectCommand, None)
    delete_object = partialmethod(_execute, commands.DeleteObjectCommand, None)
    list_objects = partialmethod(_execute, commands.ListObjectsCommand, None)
    list_logged_objects = partialmethod(_execute, commands.ListObjectsCommand, {codec.STRIP_UNLOGGED_KEY: True})
    list_stored_objects = partialmethod(_execute, commands.ListStoredObjectsCommand, None)
    clear_objects = partialmethod(_execute, commands.ClearObjectsCommand, None)
    factory_reset = partialmethod(_execute, commands.FactoryResetCommand, None)
    reboot = partialmethod(_execute, commands.RebootCommand, None)
    list_compatible_objects = partialmethod(_execute, commands.ListCompatibleObjectsCommand, None)
    discover_objects = partialmethod(_execute, commands.DiscoverObjectsCommand, None)


def setup(app: web.Application):
    features.add(app, SparkController(name=app['config']['name'], app=app))


def get_controller(app: web.Application) -> SparkController:
    return features.get(app, SparkController)
