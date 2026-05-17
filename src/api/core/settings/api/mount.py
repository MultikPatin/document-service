from pydantic import Field
from pydantic_settings import BaseSettings

from src.api.core.constants import MountedDefaults


class MountSettings(BaseSettings):
    TITLE: str = Field(
        default=MountedDefaults.TITLE,
        description="Title of the api",
        max_length=128,
    )
    DESCRIPTION: str = Field(
        default=MountedDefaults.DESCRIPTION,
        description="Description of the api",
        max_length=255,
    )
    VERSION: int = Field(
        default=1,
        description="Version of the api",
        gt=0,
        le=99,
    )
    IS_STATIC_DOCS: bool = Field(
        default=MountedDefaults.IS_STATIC_DOCS,
        description="Enable static api documentation assets",
    )
