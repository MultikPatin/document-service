from typing import Any

from pydantic import Field
from pydantic_settings import BaseSettings

from .constants import (
    ReadConcernDefaults,
    ReadConcernKeys,
    ReadConcernLevelEnum,
)


class ReadConcernSettings(BaseSettings):
    LEVEL: ReadConcernLevelEnum = Field(
        default=ReadConcernDefaults.LEVEL,
        description="Read concern level: local, majority, linearizable",
        min_length=1,
    )

    @property
    def client_kwargs(self) -> dict[str, Any]:
        """Returns a dictionary with parameters for creating an AsyncMongoClient
        instance.
        """
        d: dict[str, Any] = {}

        d[ReadConcernKeys.LEVEL] = self.LEVEL.value

        return d
