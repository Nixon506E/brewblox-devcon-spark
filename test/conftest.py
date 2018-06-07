"""
Master file for pytest fixtures.
Any fixtures declared here are available to all test functions in this directory.
"""


import logging
import os

import pytest
from brewblox_devcon_spark.__main__ import create_parser
from brewblox_service import brewblox_logger, service, features

LOGGER = brewblox_logger(__name__)


@pytest.fixture(scope='session', autouse=True)
def log_enabled():
    """Sets log level to DEBUG for all test functions.
    Allows all logged messages to be captured during pytest runs"""
    logging.getLogger().setLevel(logging.DEBUG)


@pytest.fixture
def app_config() -> dict:
    return {
        'name': 'test_app',
        'host': 'localhost',
        'port': 1234,
        'debug': True,
        'database': 'test_db.json',
        'system_database': 'brewblox_sys_db.json',
        'device_port': '/dev/TESTEH',
        'device_id': '1234',
        'simulation': False,
        'broadcast_interval': 5,
        'broadcast_exchange': 'brewcast',
    }


@pytest.fixture
def sys_args(app_config) -> list:
    return [
        'app_name',
        '--debug',
        '--name', app_config['name'],
        '--host', app_config['host'],
        '--port', str(app_config['port']),
        '--database', app_config['database'],
        '--system-database', app_config['system_database'],
        '--device-port', app_config['device_port'],
        '--device-id', app_config['device_id'],
        '--broadcast-interval', str(app_config['broadcast_interval']),
        '--broadcast-exchange', app_config['broadcast_exchange'],
    ]


@pytest.fixture
def app(sys_args):
    parser = create_parser('default')
    app = service.create_app(parser=parser, raw_args=sys_args[1:])
    return app


@pytest.fixture
def client(app, aiohttp_client, loop):
    """Allows patching the app or aiohttp_client before yielding it.

    Any tests wishing to add custom behavior to app can override the fixture
    """
    LOGGER.debug('Available features:')
    for name, impl in app.get(features.FEATURES_KEY, {}).items():
        LOGGER.debug(f'Feature "{name}" = {impl}')
    LOGGER.debug(app.on_startup)

    return loop.run_until_complete(aiohttp_client(app))


@pytest.fixture(scope='session', autouse=True)
def remove_test_db():
    """
    Automatically removes the test database file after a full run.
    """
    yield None
    try:
        os.remove('test_db.json')
    except FileNotFoundError:
        pass
