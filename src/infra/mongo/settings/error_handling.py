from pydantic import Field
from pydantic_settings import BaseSettings

from src.infra.mongo.annotations import ClientKwargsType
from src.infra.mongo.constants.settings import (
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
    def client_kwargs(self) -> ClientKwargsType:
        """Returns a dictionary with parameters for creating an AsyncMongoClient
        instance.
        """
        d: ClientKwargsType = {
            ErrorHandlingKeys.UNICODE_DECODE: self.UNICODE_DECODE.value
        }

        return d
