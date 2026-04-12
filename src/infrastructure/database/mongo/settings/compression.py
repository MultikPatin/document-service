from typing import Any

from pydantic import Field, NonNegativeInt
from pydantic_settings import BaseSettings

from .constants import CompressionDefaults, CompressionKeys, CompressorsEnum


class CompressionSettings(BaseSettings):
    COMPRESSORS: CompressorsEnum | None = Field(
        default=CompressionDefaults.COMPRESSORS,
        description="Compression method: snappy, zlib, zstd",
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
        d: dict[str, Any] = {}

        if self.COMPRESSORS:
            d[CompressionKeys.COMPRESSORS] = self.COMPRESSORS.value
        if self.ZLIB_COMPRESSION_LEVEL:
            d[CompressionKeys.ZLIB_COMPRESSION_LEVEL] = (
                self.ZLIB_COMPRESSION_LEVEL
            )

        return d
