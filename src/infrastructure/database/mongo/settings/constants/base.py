from typing import Final, Literal, final


@final
class BaseDefaults:
    ENV_FILE: Final[str] = ".env"
    ENV_PREFIX: Final[str] = "MONGODB_"
    ENV_FILE_ENCODING: Final[str] = "utf-8"
    ENV_NESTED_DELIMITER: Final[str] = "__"
    EXTRA: Final[Literal["allow", "ignore", "forbid"]] = "ignore"
    FROZEN: Final[bool] = True
    DB_NAME: Final[str] = "default-db"
