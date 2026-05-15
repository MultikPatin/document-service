from pydantic import Field
from pydantic_settings import BaseSettings

from src.infra.mongo.annotations import ClientKwargsType
from src.infra.mongo.constants.settings import (
    ReadConcernDefaults,
    ReadConcernKeys,
    ReadConcernLevelEnum,
)


class ReadSettings(BaseSettings):
    LEVEL: ReadConcernLevelEnum = Field(
        default=ReadConcernDefaults.LEVEL,
        description="Read concern level: local, majority, linearizable",
        min_length=1,
    )

    @property
    def client_kwargs(self) -> ClientKwargsType:
        """Returns a dictionary with parameters for creating an AsyncMongoClient
        instance.
        """
        d: ClientKwargsType = {ReadConcernKeys.LEVEL: self.LEVEL.value}

        return d
