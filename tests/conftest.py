pytest_plugins = [
    # tests.unit.infrastructure.database.mongo.settings
    "tests.unit.infrastructure.database.mongo.settings.fixtures.authentication_fixtures",
    "tests.unit.infrastructure.database.mongo.settings.fixtures.composite_fixtures",
    "tests.unit.infrastructure.database.mongo.settings.fixtures.compression_fixtures",
    "tests.unit.infrastructure.database.mongo.settings.fixtures.connection_fixtures",
    "tests.unit.infrastructure.database.mongo.settings.fixtures.connection_mode_fixtures",
    "tests.unit.infrastructure.database.mongo.settings.fixtures.error_handling_fixtures",
    "tests.unit.infrastructure.database.mongo.settings.fixtures.pool_fixtures",
    "tests.unit.infrastructure.database.mongo.settings.fixtures.read_concern_fixtures",
    "tests.unit.infrastructure.database.mongo.settings.fixtures.representation_fixtures",
    "tests.unit.infrastructure.database.mongo.settings.fixtures.retry_behavior_fixtures",
    "tests.unit.infrastructure.database.mongo.settings.fixtures.srv_fixtures",
    "tests.unit.infrastructure.database.mongo.settings.fixtures.timeouts_fixtures",
    "tests.unit.infrastructure.database.mongo.settings.fixtures.write_concern_fixtures",
    "tests.unit.infrastructure.database.mongo.settings.fixtures.tls_fixtures",
    # tests.unit.infrastructure.database.mongo.converters
    "tests.unit.infrastructure.database.mongo.converters.fixtures.id_fixtures",
]
