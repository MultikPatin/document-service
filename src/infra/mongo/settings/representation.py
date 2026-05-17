from pydantic import Field
from pydantic_settings import BaseSettings

from src.infra.mongo.annotations import ClientKwargsType
from src.infra.mongo.constants.settings import (
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
    def client_kwargs(self) -> ClientKwargsType:
        """Returns a dictionary with parameters for creating an AsyncMongoClient
        instance.
        """
        d: ClientKwargsType = {RepresentationKeys.UUID: self.UUID.value}

        return d
