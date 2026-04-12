from enum import StrEnum
from typing import Final, final


class CompressorsEnum(StrEnum):
    SNAPPY = "snappy"
    ZLIB = "zlib"
    ZSTD = "zstd"


@final
class CompressionDefaults:
    COMPRESSORS: Final[CompressorsEnum | None] = None
    ZLIB_COMPRESSION_LEVEL: Final[int | None] = None


@final
class CompressionKeys:
    COMPRESSORS = "compressors"
    ZLIB_COMPRESSION_LEVEL = "zlibCompressionLevel"
