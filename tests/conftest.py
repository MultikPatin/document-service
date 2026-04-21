from typing import Final

MONGODB: Final[str] = "tests.unit.adapters.database.mongo."
MONGODB_SETTINGS: Final[str] = MONGODB + "settings.fixtures."
MONGODB_CONVERTERS: Final[str] = MONGODB + "converters.fixtures."

pytest_plugins: Final[list[str]] = [
    MONGODB_SETTINGS + "authentication",
    MONGODB_SETTINGS + "composite",
    MONGODB_SETTINGS + "compression",
    MONGODB_SETTINGS + "connection",
    MONGODB_SETTINGS + "connection_mode",
    MONGODB_SETTINGS + "error_handling",
    MONGODB_SETTINGS + "pool",
    MONGODB_SETTINGS + "read_concern",
    MONGODB_SETTINGS + "representation",
    MONGODB_SETTINGS + "retry_behavior",
    MONGODB_SETTINGS + "srv",
    MONGODB_SETTINGS + "timeouts",
    MONGODB_SETTINGS + "write_concern",
    MONGODB_SETTINGS + "tls",
    MONGODB_CONVERTERS + "id",
]
