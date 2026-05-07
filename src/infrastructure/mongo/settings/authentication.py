from pydantic import Field
from pydantic_settings import BaseSettings

from src.infrastructure.mongo.annotations import ClientKwargsType
from src.infrastructure.mongo.constants.settings import (
    AuthenticationDefaults,
    AuthenticationKeys,
    AuthenticationMechanismEnum,
)


class AuthenticationSettings(BaseSettings):
    SOURCE: str = Field(
        default=AuthenticationDefaults.SOURCE,
        description="Database to authenticate against",
        min_length=1,
        max_length=64,
    )
    MECHANISM: AuthenticationMechanismEnum = Field(
        default=AuthenticationDefaults.MECHANISM,
        description="Authentication mechanism",
    )
    MECHANISM_PROPERTIES: str | None = Field(
        default=AuthenticationDefaults.MECHANISM_PROPERTIES,
        description="Authentication mechanism properties",
    )

    @property
    def client_kwargs(self) -> ClientKwargsType:
        """Returns a dictionary with parameters for creating an AsyncMongoClient
        instance.
        """
        d: ClientKwargsType = {
            AuthenticationKeys.SOURCE: self.SOURCE,
            AuthenticationKeys.MECHANISM: self.MECHANISM.value,
            AuthenticationKeys.MECHANISM_PROPERTIES: self.MECHANISM_PROPERTIES,
        }

        return d
