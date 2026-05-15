from pydantic import Field
from pydantic_settings import BaseSettings

from src.api.constants import API_ENV_PREFIX, BaseDefaults
from src.domain.utils import settings_model_config

from .gzip import GzipSettings


class Settings(BaseSettings):
    model_config = settings_model_config(env_prefix=API_ENV_PREFIX)

    IS_DEV_MODE: bool = Field(
        default=BaseDefaults.IS_DEV_MODE,
        description="Is Development Mode",
    )

    ALLOW_ORIGINS: list[str] = Field(
        default=BaseDefaults.ALLOW_ORIGINS,
        description="Allow origins",
        min_length=1,
    )
    ALLOW_HEADERS: list[str] = Field(
        default=BaseDefaults.ALLOW_HEADERS,
        description="Allow headers",
        min_length=1,
    )
    ALLOW_METHODS: list[str] = Field(
        default=BaseDefaults.ALLOW_METHODS,
        description="Allow methods",
        min_length=1,
    )

    gzip: GzipSettings = GzipSettings()
