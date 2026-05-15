from pydantic import Field
from pydantic_settings import BaseSettings

from src.api.constants import GzipDefaults


class GzipSettings(BaseSettings):
    ENABLE: bool = Field(
        default=GzipDefaults.ENABLE,
        description="Is Gzip Compressed",
    )
    MIN_SIZE: int = Field(
        default=GzipDefaults.MIN_SIZE,
        description="Gzip min compressed size",
        gt=100,
        lt=1024 * 10,
    )
    COMPRESS_LEVEL: int = Field(
        default=GzipDefaults.COMPRESS_LEVEL,
        description="Gzip compress level",
        gt=0,
        le=9,
    )
