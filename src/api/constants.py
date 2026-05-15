from typing import Final, final

API_ENV_PREFIX: Final[str] = "API_"
STORAGE_API_ENV_PREFIX = "STORAGE_"
CONSTRUCTOR_API_ENV_PREFIX = "CONSTRUCTOR_"


@final
class BaseDefaults:
    IS_DEV_MODE: bool = True

    ALLOW_ORIGINS: Final[list[str]] = ["*"]
    ALLOW_HEADERS: Final[list[str]] = ["*"]
    ALLOW_METHODS: Final[list[str]] = ["*"]


@final
class GzipDefaults:
    ENABLE: Final[bool] = True
    MIN_SIZE: Final[int] = 500
    COMPRESS_LEVEL: Final[int] = 6
