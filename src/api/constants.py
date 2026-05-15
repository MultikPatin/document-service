from typing import Final, final

API_ENV_PREFIX: Final[str] = "API_"
STORAGE_API_ENV_PREFIX: Final[str] = "STORAGE_"
CONSTRUCTOR_API_ENV_PREFIX: Final[str] = "CONSTRUCTOR_"

API_HEADER_PROCESS_TIME: Final[str] = "X-Process-Time"


@final
class BaseDefaults:
    IS_DEV_MODE: Final[bool] = True
    IS_STATIC_DOCS: Final[bool] = True

    ALLOW_ORIGINS: Final[list[str]] = ["*"]
    ALLOW_HEADERS: Final[list[str]] = ["*"]
    ALLOW_METHODS: Final[list[str]] = ["*"]
    ROOT_PATH: Final[str] = "api"


@final
class GzipDefaults:
    ENABLE: Final[bool] = True
    MIN_SIZE: Final[int] = 500
    COMPRESS_LEVEL: Final[int] = 6
