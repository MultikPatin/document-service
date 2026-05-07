from pydantic import Field
from pydantic_settings import BaseSettings

from src.infrastructure.mongo.annotations import ClientKwargsType
from src.infrastructure.mongo.constants.settings import (
    WriteConcernDefaults,
    WriteConcernKeys,
)


class WriteSettings(BaseSettings):
    W: int | str | None = Field(
        default=WriteConcernDefaults.W,
        description="Write concern: number of replicas or 'majority'",
    )
    JOURNAL: bool = Field(
        default=WriteConcernDefaults.JOURNAL,
        description="Wait for write to be written to journal",
    )
    FSYNC: bool = Field(
        default=WriteConcernDefaults.FSYNC,
        description="Force the write operation to fsync to disk",
    )

    @property
    def client_kwargs(self) -> ClientKwargsType:
        """Returns a dictionary with parameters for creating an AsyncMongoClient
        instance.
        """
        d: ClientKwargsType = {
            WriteConcernKeys.JOURNAL: self.JOURNAL,
            WriteConcernKeys.FSYNC: self.FSYNC,
        }

        if self.W:
            d[WriteConcernKeys.W] = self.W

        return d
