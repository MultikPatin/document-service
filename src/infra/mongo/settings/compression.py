from typing import Any

from pydantic import Field, NonNegativeInt, ValidationError, field_validator
from pydantic_settings import BaseSettings

from src.infra.mongo.annotations import ClientKwargsType
from src.infra.mongo.constants.settings import (
    CompressionDefaults,
    CompressionKeys,
    CompressorsEnum,
)


class CompressionSettings(BaseSettings):
    COMPRESSORS: CompressorsEnum | list[CompressorsEnum] | None = Field(
        default=CompressionDefaults.COMPRESSORS,
        description="Comma separated list of compressors for wire"
        "protocol compression. The list is used to negotiate a compressor"
        "with the server. Currently supported options are 'snappy', 'zlib'"
        "and 'zstd'",
    )
    ZLIB_COMPRESSION_LEVEL: NonNegativeInt | None = Field(
        default=CompressionDefaults.ZLIB_COMPRESSION_LEVEL,
        description="zlib compression level (0-9)",
        le=9,
    )

    @field_validator("COMPRESSORS", mode="before")
    @classmethod
    def sanitize_compressors(
        cls,
        value: Any,  # noqa: ANN401
    ) -> CompressorsEnum | list[CompressorsEnum] | None:
        if value is None:
            return None
        if not isinstance(value, str):
            msg = f"Compressors value {value} is not a string"
            raise ValidationError(msg)

        items = value.split(",")
        if len(items) == 1:
            return CompressorsEnum(items[0])
        return [CompressorsEnum(item) for item in items]

    @property
    def compressors_string(self) -> str | None:
        if isinstance(self.COMPRESSORS, CompressorsEnum):
            return str(self.COMPRESSORS)
        if isinstance(self.COMPRESSORS, list):
            return ",".join(self.COMPRESSORS)
        return None

    @property
    def client_kwargs(self) -> ClientKwargsType:
        """Returns a dictionary with parameters for creating an AsyncMongoClient
        instance.
        """
        d: ClientKwargsType = {}

        if self.COMPRESSORS:
            d[CompressionKeys.COMPRESSORS] = self.compressors_string
        if self.ZLIB_COMPRESSION_LEVEL:
            d[CompressionKeys.ZLIB_COMPRESSION_LEVEL] = (
                self.ZLIB_COMPRESSION_LEVEL
            )

        return d
