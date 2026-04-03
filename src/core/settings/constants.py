from typing import Any, Final, final

_MODEL_CONFIG_DEFAULTS: Final[dict[str, Any]] = {
    "env_file": ".env",
    "env_file_encoding": "utf-8",
    "env_nested_delimiter": "__",
    "extra": "ignore",
    "frozen": True,
}


@final
class PostgresDefaults:
    ENV_PREFIX: Final[str] = "POSTGRES_"
    PORT: Final[int] = 5432
    SCHEMA: Final[str] = "postgresql"
