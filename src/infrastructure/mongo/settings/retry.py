from pydantic import Field
from pydantic_settings import BaseSettings

from libs.mongo.constants.settings import (
    RetryBehaviorDefaults,
    RetryBehaviorKeys,
)
from src.infrastructure.mongo.annotations import ClientKwargsType


class RetrySettings(BaseSettings):
    WRITES: bool = Field(
        default=RetryBehaviorDefaults.WRITES,
        description="Enable retryable writes",
    )
    READS: bool = Field(
        default=RetryBehaviorDefaults.READS,
        description="Enable retryable reads",
    )

    @property
    def client_kwargs(self) -> ClientKwargsType:
        """Returns a dictionary with parameters for creating an AsyncMongoClient
        instance.
        """
        d: ClientKwargsType = {
            RetryBehaviorKeys.WRITES: self.WRITES,
            RetryBehaviorKeys.READS: self.READS,
        }

        return d
