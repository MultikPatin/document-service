from typing import Final, final

API_ENV_PREFIX: Final[str] = "API_CORE_"
API_HEADER_PROCESS_TIME: Final[str] = "X-Process-Time"


@final
class CoreDefaults:
    IS_DEV_MODE: Final[bool] = True

    ALLOW_ORIGINS: Final[list[str]] = ["*"]
    ALLOW_HEADERS: Final[list[str]] = ["*"]
    ALLOW_METHODS: Final[list[str]] = ["*"]
    ROOT_PATH: Final[str] = "api"


@final
class MountedDefaults:
    IS_STATIC_DOCS: Final[bool] = True
    TITLE: Final[str] = "Please set api title"
    DESCRIPTION: Final[str] = "Please set api description"


@final
class GzipDefaults:
    ENABLE: Final[bool] = True
    MIN_SIZE: Final[int] = 500
    COMPRESS_LEVEL: Final[int] = 6
