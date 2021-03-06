"""
Example of how to import and use the brewblox service
"""

import logging
from configparser import ConfigParser
from os import getenv

from brewblox_service import brewblox_logger, http, mqtt, scheduler, service

from brewblox_devcon_spark import (block_cache, block_store, broadcaster,
                                   commander, config_store, connection,
                                   service_status, simulator, spark,
                                   synchronization)
from brewblox_devcon_spark.api import (blocks_api, debug_api, error_response,
                                       mqtt_api, settings_api, sim_api,
                                       system_api)
from brewblox_devcon_spark.codec import codec, unit_conversion

LOGGER = brewblox_logger(__name__)


def create_parser(default_name='spark'):
    parser = service.create_parser(default_name=default_name)

    # Device options
    group = parser.add_argument_group('Device communication')
    group.add_argument('--simulation',
                       help='Start in simulation mode. Will not connect to a physical device. '
                       'This option takes precedence over other connection options. '
                       'The simulator is assigned the --device-id value if set or 123456789012345678901234. '
                       'If you are using multiple simulators, you need to assign them unique device IDs. '
                       '[%(default)s]',
                       action='store_true')
    group.add_argument('--device-host',
                       help='Spark device URL host. '
                       'Will only connect if device ID matches advertised ID, or is not set. [%(default)s]')
    group.add_argument('--device-port',
                       help='Spark device URL port when accessing a device over WiFi. [%(default)s]',
                       type=int,
                       default=8332)
    group.add_argument('--device-serial',
                       help='Spark device serial port. Takes precedence over URL connections. '
                       'Will only connect if device ID matches advertised ID, or is not set. [%(default)s]')
    group.add_argument('--device-id',
                       help='Spark serial number. Any spark is valid if not set. [%(default)s]')
    group.add_argument('--discovery',
                       help='Enabled types of device discovery. '
                       '--device-serial and --device-host disable discovery. '
                       '--device-id specifies which discovered device is valid. ',
                       choices=['all', 'usb', 'wifi'],
                       default='all')

    # Service network options
    group = parser.add_argument_group('Service communication')
    group.add_argument('--command-timeout',
                       help='Timeout period (in seconds) for controller commands. [$(default)s]',
                       type=float,
                       default=20)
    group.add_argument('--broadcast-interval',
                       help='Interval (in seconds) between broadcasts of controller state. '
                       'Set to a value <= 0 to disable broadcasting. [%(default)s]',
                       type=float,
                       default=5)
    group.add_argument('--volatile',
                       action='store_true',
                       help='Disable all outgoing network calls. [%(default)s]')

    # Updater options
    group = parser.add_argument_group('Firmware')
    group.add_argument('--skip-version-check',
                       help='Skip firmware version check: will not raise error on mismatch',
                       action='store_true')

    return parser


def parse_ini(app):  # pragma: no cover
    parser = ConfigParser()
    parser.read('binaries/firmware.ini')
    config = dict(parser['FIRMWARE'].items())
    LOGGER.info(f'firmware.ini: {config}')
    return config


def main():
    app = service.create_app(parser=create_parser())
    logging.captureWarnings(True)
    config = app['config']
    app['ini'] = parse_ini(app)

    if getenv('ENABLE_DEBUGGER', False):  # pragma: no cover
        import debugpy
        debugpy.listen(('0.0.0.0', 5678))
        LOGGER.info('Debugger is enabled and listening on 5678')

    if config['simulation']:
        config['device_id'] = config['device_id'] or '123456789012345678901234'
        config['device_host'] = 'localhost'
        config['device_port'] = 8332
        config['device_serial'] = None
        simulator.setup(app)

    service_status.setup(app)
    http.setup(app)

    connection.setup(app)
    commander.setup(app)

    scheduler.setup(app)
    mqtt.setup(app)

    config_store.setup(app)
    block_store.setup(app)
    block_cache.setup(app)
    unit_conversion.setup(app)
    codec.setup(app)
    spark.setup(app)
    broadcaster.setup(app)

    error_response.setup(app)
    debug_api.setup(app)
    blocks_api.setup(app)
    system_api.setup(app)
    settings_api.setup(app)
    mqtt_api.setup(app)

    if config['simulation']:
        sim_api.setup(app)

    synchronization.setup(app)

    service.furnish(app)
    service.run(app)


if __name__ == '__main__':
    main()
