from enum import StrEnum
from typing import Final, final


class ErrorHandlingUnicodeDecodeEnum(StrEnum):
    strict = "strict"
    ignore = "ignore"
    replace = "replace"
    backslashreplace = "backslashreplace"
    surrogate_escape = "surrogateescape"


@final
class ErrorHandlingDefaults:
    UNICODE_DECODE: Final[ErrorHandlingUnicodeDecodeEnum] = (
        ErrorHandlingUnicodeDecodeEnum.strict
    )


@final
class ErrorHandlingKeys:
    UNICODE_DECODE = "unicode_decode_error_handler"
