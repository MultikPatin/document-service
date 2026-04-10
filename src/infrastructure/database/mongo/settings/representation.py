from typing import Any

from pydantic import Field
from pydantic_settings import BaseSettings

from .constants import (
    RepresentationDefaults,
    RepresentationKeys,
    RepresentationUuidEnum,
)


class RepresentationSettings(BaseSettings):
    UUID: RepresentationUuidEnum = Field(
        default=RepresentationDefaults.UUID,
        description="UUID representation format",
    )

    @property
    def client_kwargs(self) -> dict[str, Any]:
        """Returns a dictionary with parameters for creating an AsyncMongoClient
        instance.
        """
        d: dict[str, Any] = {}

        d[RepresentationKeys.UUID] = self.UUID

        return d
