from typing import Any

from pydantic import Field, NonNegativeInt
from pydantic_settings import BaseSettings

from .constants import CompressionDefaults


class CompressionSettings(BaseSettings):
    COMPRESSORS: str | None = Field(
        default=CompressionDefaults.COMPRESSORS,
        description="Compression method: snappy, zlib, zstd",
        pattern="^(snappy|zlib|zstd)?$",
    )
    ZLIB_COMPRESSION_LEVEL: NonNegativeInt | None = Field(
        default=CompressionDefaults.ZLIB_COMPRESSION_LEVEL,
        description="zlib compression level (0-9)",
        le=9,
    )

    @property
    def client_kwargs(self) -> dict[str, Any]:
        """Returns a dictionary with parameters for creating an AsyncMongoClient
        instance.
        """
        result: dict[str, Any] = {}

        if self.COMPRESSORS:
            result["compressors"] = self.COMPRESSORS
        if self.ZLIB_COMPRESSION_LEVEL:
            result["zlibCompressionLevel"] = self.ZLIB_COMPRESSION_LEVEL

        return result
