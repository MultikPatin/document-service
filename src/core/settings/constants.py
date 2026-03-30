from typing import Any, Final, final

from pydantic import SecretStr

MODEL_CONFIG_DEFAULTS: Final[dict[str, Any]] = {
    "env_file": ".env",
    "env_file_encoding": "utf-8",
    "env_nested_delimiter": "__",
    "extra": "ignore",
    "frozen": True,
}


@final
class Defaults:
    HOST: Final[str] = "localhost"
    USERNAME: Final[str] = ""
    PASSWORD: Final[SecretStr] = SecretStr("")
    DATABASE: Final[str] = "default-db"


@final
class PostgresDefaults:
    ENV_PREFIX: Final[str] = "POSTGRES_"
    PORT: Final[int] = 5432
    SCHEMA: Final[str] = "postgresql"
