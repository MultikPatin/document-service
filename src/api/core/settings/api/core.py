from pydantic import Field
from pydantic_settings import BaseSettings

from src.api.core.constants import API_ENV_PREFIX, CoreDefaults
from src.api.core.settings.gzip import GzipSettings
from src.domain.utils import settings_model_config


class CoreSettings(BaseSettings):
    model_config = settings_model_config(env_prefix=API_ENV_PREFIX)

    IS_DEV_MODE: bool = Field(
        default=CoreDefaults.IS_DEV_MODE,
        description="Enable development mode",
    )
    ALLOW_ORIGINS: list[str] = Field(
        default=CoreDefaults.ALLOW_ORIGINS,
        description="Allow origins",
        min_length=1,
    )
    ALLOW_HEADERS: list[str] = Field(
        default=CoreDefaults.ALLOW_HEADERS,
        description="Allow headers",
        min_length=1,
    )
    ALLOW_METHODS: list[str] = Field(
        default=CoreDefaults.ALLOW_METHODS,
        description="Allow methods",
        min_length=1,
    )
    ROOT_PATH: str = Field(
        default=CoreDefaults.ROOT_PATH,
        description="Root path of the api",
        min_length=1,
    )

    gzip: GzipSettings = GzipSettings()
