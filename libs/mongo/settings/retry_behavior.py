from typing import Any

from pydantic import Field
from pydantic_settings import BaseSettings

from libs.mongo.constants.settings import (
    RetryBehaviorDefaults,
    RetryBehaviorKeys,
)


class RetryBehaviorSettings(BaseSettings):
    WRITES: bool = Field(
        default=RetryBehaviorDefaults.WRITES,
        description="Enable retryable writes",
    )
    READS: bool = Field(
        default=RetryBehaviorDefaults.READS,
        description="Enable retryable reads",
    )

    @property
    def client_kwargs(self) -> dict[str, Any]:
        """Returns a dictionary with parameters for creating an AsyncMongoClient
        instance.
        """
        d: dict[str, Any] = {}

        d[RetryBehaviorKeys.WRITES] = self.WRITES
        d[RetryBehaviorKeys.READS] = self.READS

        return d
