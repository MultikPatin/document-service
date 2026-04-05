from typing import Any

from pydantic import Field
from pydantic_settings import BaseSettings

from .defaults import AuthenticationDefaults


class AuthenticationSettings(BaseSettings):
    SOURCE: str = Field(
        default=AuthenticationDefaults.SOURCE,
        description="Database to authenticate against",
        min_length=1,
        max_length=64,
    )
    MECHANISM: str = Field(
        default=AuthenticationDefaults.MECHANISM,
        description="Authentication mechanism",
        pattern="^(SCRAM-SHA-1|SCRAM-SHA-256)$",
    )
    # MECHANISM_PROPERTIES: str | None = Field(
    #     default=AuthenticationDefaults.MECHANISM_PROPERTIES,
    #     description="Authentication mechanism",
    #     pattern="^(SCRAM-SHA-1|SCRAM-SHA-256)$",
    # )

    @property
    def client_kwargs(self) -> dict[str, Any]:
        """Returns a dictionary with parameters for creating an AsyncMongoClient
        instance.
        """
        result: dict[str, Any] = {}

        result["authSource"] = self.SOURCE
        result["authMechanism"] = self.MECHANISM
        # result["authMechanismProperties"] = self.MECHANISM_PROPERTIES

        return result
