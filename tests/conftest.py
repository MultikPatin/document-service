pytest_plugins = [
    "tests.unit.infrastructure.database.mongo.settings.fixtures.composite_fixtures",
    "tests.unit.infrastructure.database.mongo.settings.fixtures.representation_fixtures",
    "tests.unit.infrastructure.database.mongo.settings.fixtures.srv_fixtures",
    "tests.unit.infrastructure.database.mongo.settings.fixtures.timeouts_fixtures",
    "tests.unit.infrastructure.database.mongo.settings.fixtures.write_concern_fixtures",
    "tests.unit.infrastructure.database.mongo.settings.fixtures.tls_fixtures",
    "tests.unit.infrastructure.database.mongo.converters.fixtures.id_fixtures",
]
