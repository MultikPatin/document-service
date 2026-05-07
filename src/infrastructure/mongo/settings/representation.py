from pydantic import Field
from pydantic_settings import BaseSettings

from libs.mongo.constants.settings import (
    RepresentationDefaults,
    RepresentationKeys,
    RepresentationUuidEnum,
)
from src.infrastructure.mongo.annotations import ClientKwargsType


class RepresentationSettings(BaseSettings):
    UUID: RepresentationUuidEnum = Field(
        default=RepresentationDefaults.UUID,
        description="UUID representation format",
    )

    @property
    def client_kwargs(self) -> ClientKwargsType:
        """Returns a dictionary with parameters for creating an AsyncMongoClient
        instance.
        """
        d: ClientKwargsType = {RepresentationKeys.UUID: self.UUID.value}

        return d
