from typing import Any

from pydantic import Field, NonNegativeInt
from pydantic_settings import BaseSettings

from .constants import TimeoutsDefaults


class TimeoutsSettings(BaseSettings):
    CONNECTION_MS: NonNegativeInt = Field(
        default=TimeoutsDefaults.CONNECTION_MS,
        description="Connect timeout (ms)",
    )
    SOCKET_MS: NonNegativeInt = Field(
        default=TimeoutsDefaults.SOCKET_MS,
        description="Socket timeout (ms)",
    )
    SERVER_SELECTION_MS: NonNegativeInt = Field(
        default=TimeoutsDefaults.SERVER_SELECTION_MS,
        description="Server selection timeout (ms)",
    )
    OPERATION_MS: NonNegativeInt | None = Field(
        default=TimeoutsDefaults.OPERATION_MS,
        description="Operation timeout (ms), None means no timeout",
    )

    @property
    def client_kwargs(self) -> dict[str, Any]:
        """Returns a dictionary with parameters for creating an AsyncMongoClient
        instance.
        """
        result: dict[str, Any] = {}

        result["connectTimeoutMS"] = self.CONNECTION_MS
        result["socketTimeoutMS"] = self.SOCKET_MS
        result["serverSelectionTimeoutMS"] = self.SERVER_SELECTION_MS

        if self.OPERATION_MS:
            result["timeoutMS"] = self.OPERATION_MS

        return result
