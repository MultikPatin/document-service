from typing import Any

from pydantic import Field
from pydantic_settings import BaseSettings

from libs.mongo.constants.settings import WriteConcernDefaults, WriteConcernKeys


class WriteConcernSettings(BaseSettings):
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
    def client_kwargs(self) -> dict[str, Any]:
        """Returns a dictionary with parameters for creating an AsyncMongoClient
        instance.
        """
        d: dict[str, Any] = {}

        d[WriteConcernKeys.JOURNAL] = self.JOURNAL
        d[WriteConcernKeys.FSYNC] = self.FSYNC

        if self.W:
            d[WriteConcernKeys.W] = self.W

        return d
