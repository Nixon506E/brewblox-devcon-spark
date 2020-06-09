"""
Tests brewblox_devcon_spark.device
"""

import pytest
from brewblox_service import features, scheduler
from mock import AsyncMock

from brewblox_devcon_spark import (commander, commander_sim, const, datastore,
                                   device, exceptions, state)
from brewblox_devcon_spark.codec import codec, unit_conversion

TESTED = device.__name__


def generate_obj():
    return 'EdgeCase', {
        'settings': {
            'address': 'ff'.rjust(16, '0'),
            'offset[delta_degC]': 20
        },
        'state': {
            'value[delta_degC]': 123,
            'connected': True
        },
        'link<ActuatorAnalogInterface>': 30,
        'additionalLinks': [
            {'connection<TempSensorInterface>': 1},
            {'connection<TempSensorInterface>': 2},
        ],
        'listValues': [1, 2, 3],
    }


@pytest.fixture
def app(app):
    """App + controller routes"""
    state.setup(app)
    datastore.setup(app)
    commander_sim.setup(app)
    scheduler.setup(app)
    unit_conversion.setup(app)
    codec.setup(app)
    device.setup(app)
    return app


@pytest.fixture
def cmder(app):
    return features.get(app, commander.SparkCommander)


@pytest.fixture
def ctrl(app):
    return device.get_controller(app)


@pytest.fixture
async def store(app, client):
    return datastore.get_block_store(app)


async def test_transcoding(app, client, cmder, store, ctrl):
    c = codec.get_codec(app)
    obj_type, obj_data = generate_obj()
    enc_type, enc_data = await c.encode(obj_type, obj_data)

    object_args = {
        'id': 'alias',
        'groups': [1],
        'type': obj_type,
        'data': obj_data
    }

    store['alias', 300] = dict()

    c.encode = AsyncMock(wraps=c.encode)
    c.decode = AsyncMock(wraps=c.decode)

    retval = await ctrl.create_object(object_args)
    assert retval['data']['settings']['address'] == 'ff'.rjust(16, '0')

    c.encode.assert_any_await(obj_type, obj_data, opts=None)
    c.decode.assert_any_await(enc_type, enc_data, opts=None)


async def test_list_transcoding(app, client, cmder, store, ctrl, mocker):
    obj_type, obj_data = generate_obj()
    ids = {f'obj{i}' for i in range(5)}

    for i, id in enumerate(ids):
        store[id, 300+i] = dict()

        await ctrl.create_object({
            'id': id,
            'groups': [0],
            'type': obj_type,
            'data': obj_data
        })

    retval = await ctrl.list_stored_objects()
    assert ids.issubset({obj['id'] for obj in retval['objects']})


async def test_convert_id(app, client, store, mocker, ctrl):
    store['alias', 123] = dict()
    store['4-2', 24] = dict()

    resolver = device.SparkResolver(app)

    assert await resolver.convert_sid_nid({'id': 'alias'}) == {'nid': 123}
    assert await resolver.convert_sid_nid({'nid': 840}) == {'nid': 840}
    assert await resolver.convert_sid_nid({'id': 840}) == {'nid': 840}
    # When both present, NID takes precedence
    assert await resolver.convert_sid_nid({'id': 'alias', 'nid': 444}) == {'nid': 444}
    assert await resolver.convert_sid_nid({}) == {}

    assert await resolver.add_sid({'nid': 123}) == {'nid': 123, 'id': 'alias'}
    assert await resolver.add_sid({'id': 'testey'}) == {'id': 'testey'}
    assert await resolver.add_sid({}) == {}

    with pytest.raises(exceptions.DecodeException):
        await resolver.add_sid({'nid': 'testey'})

    # Service ID not found: create placeholder
    generated = await resolver.add_sid({'nid': 456, 'type': 'Edgecase,driven'})
    assert generated['id'].startswith(const.GENERATED_ID_PREFIX)
    assert ',driven' not in generated['id']


async def test_resolve_links(app, client, store):
    store['eeney', 9001] = dict()
    store['miney', 9002] = dict()
    store['moo', 9003] = dict()

    def create_data():
        return {
            'data': {
                'testval': 1,
                'input<ProcessValueInterface>': 'eeney',
                'output<ProcessValueInterface>': 'miney',
                'nested': {
                    'flappy<>': 'moo',
                    'meaning_of_life': 42,
                    'mystery<EdgeCase>': None
                },
                'listed': [
                    {'flappy<SetpointSensorPairInterface>': 'moo'}
                ]
            }
        }

    resolver = device.SparkResolver(app)
    output = await resolver.convert_links_nid(create_data())

    assert output == {
        'data': {
            'testval': 1,
            'input<ProcessValueInterface>': 9001,
            'output<ProcessValueInterface>': 9002,
            'nested': {
                'flappy<>': 9003,
                'meaning_of_life': 42,
                'mystery<EdgeCase>': 0,
            },
            'listed': [
                {'flappy<SetpointSensorPairInterface>': 9003},
            ],
        },
    }

    output = await resolver.convert_links_sid(output)
    assert output == create_data()
