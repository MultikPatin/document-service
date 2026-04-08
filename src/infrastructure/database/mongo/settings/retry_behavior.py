from typing import Any

from pydantic import Field
from pydantic_settings import BaseSettings

from .constants import RetryBehaviorDefaults


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
        result: dict[str, Any] = {}

        result["retryWrites"] = self.WRITES
        result["retryReads"] = self.READS

        return result
