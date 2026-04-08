from typing import Any

from pydantic import Field
from pydantic_settings import BaseSettings

from .constants import RepresentationDefaults


class RepresentationSettings(BaseSettings):
    UUID: str = Field(
        default=RepresentationDefaults.UUID,
        description="UUID representation format",
        pattern="^(standard|pythonLegacy|javaLegacy|csharpLegacy|unspecified)$",
    )

    @property
    def client_kwargs(self) -> dict[str, Any]:
        """Returns a dictionary with parameters for creating an AsyncMongoClient
        instance.
        """
        result: dict[str, Any] = {}

        result["uuidRepresentation"] = self.UUID

        return result
