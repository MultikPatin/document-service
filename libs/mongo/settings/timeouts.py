from typing import Any

from pydantic import Field, NonNegativeInt
from pydantic_settings import BaseSettings

from libs.mongo.constants.settings import TimeoutsDefaults, TimeoutsKeys


class TimeoutsSettings(BaseSettings):
    CONNECTION_MS: NonNegativeInt = Field(
        default=TimeoutsDefaults.CONNECTION,
        description="Connect timeout (ms)",
    )
    SOCKET_MS: NonNegativeInt = Field(
        default=TimeoutsDefaults.SOCKET,
        description="Socket timeout (ms)",
    )
    SERVER_SELECTION_MS: NonNegativeInt = Field(
        default=TimeoutsDefaults.SERVER_SELECTION,
        description="Server selection timeout (ms)",
    )
    OPERATION_MS: NonNegativeInt | None = Field(
        default=TimeoutsDefaults.OPERATION,
        description="Operation timeout (ms), None means no timeout",
    )

    @property
    def client_kwargs(self) -> dict[str, Any]:
        """Returns a dictionary with parameters for creating an AsyncMongoClient
        instance.
        """
        d: dict[str, Any] = {}

        d[TimeoutsKeys.CONNECTION] = self.CONNECTION_MS
        d[TimeoutsKeys.SOCKET] = self.SOCKET_MS
        d[TimeoutsKeys.SERVER_SELECTION] = self.SERVER_SELECTION_MS

        if self.OPERATION_MS:
            d[TimeoutsKeys.OPERATION] = self.OPERATION_MS

        return d
