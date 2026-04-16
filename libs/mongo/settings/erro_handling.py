from typing import Any

from pydantic import Field
from pydantic_settings import BaseSettings

from libs.mongo.constants.settings import (
    ErrorHandlingDefaults,
    ErrorHandlingKeys,
    ErrorHandlingUnicodeDecodeEnum,
)


class ErrorHandlingSettings(BaseSettings):
    UNICODE_DECODE: ErrorHandlingUnicodeDecodeEnum = Field(
        default=ErrorHandlingDefaults.UNICODE_DECODE,
        description="Handler for Unicode decode errors: "
        "strict, ignore, replace",
    )

    @property
    def client_kwargs(self) -> dict[str, Any]:
        """Returns a dictionary with parameters for creating an AsyncMongoClient
        instance.
        """
        d: dict[str, Any] = {}

        d[ErrorHandlingKeys.UNICODE_DECODE] = self.UNICODE_DECODE.value

        return d
