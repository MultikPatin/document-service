from typing import Any

from pydantic import Field
from pydantic_settings import BaseSettings

from .defaults import ErrorHandlingDefaults


class ErrorHandlingSettings(BaseSettings):
    UNICODE_DECODE: str = Field(
        default=ErrorHandlingDefaults.UNICODE_DECODE,
        description="Handler for Unicode decode errors: "
        "strict, ignore, replace",
        pattern="^(strict|ignore|replace|backslashreplace|surrogateescape)$",
    )

    @property
    def client_kwargs(self) -> dict[str, Any]:
        """Returns a dictionary with parameters for creating an AsyncMongoClient
        instance.
        """
        result: dict[str, Any] = {}

        result["unicode_decode_error_handler"] = self.UNICODE_DECODE

        return result
