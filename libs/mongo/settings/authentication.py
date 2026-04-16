from typing import Any

from pydantic import Field
from pydantic_settings import BaseSettings

from libs.mongo.constants.settings import (
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
    # MECHANISM_PROPERTIES: str | None = Field(
    #     default=AuthenticationDefaults.MECHANISM_PROPERTIES,
    #     description="Authentication mechanism properties",
    # )

    @property
    def client_kwargs(self) -> dict[str, Any]:
        """Returns a dictionary with parameters for creating an AsyncMongoClient
        instance.
        """
        d: dict[str, Any] = {}

        d[AuthenticationKeys.SOURCE] = self.SOURCE
        d[AuthenticationKeys.MECHANISM] = self.MECHANISM.value
        # result[AuthenticationKeys.MECHANISM_PROPERTIES] = (
        #     self.MECHANISM_PROPERTIES
        # )

        return d
