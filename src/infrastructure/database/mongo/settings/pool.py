from typing import Any

from pydantic import Field, NonNegativeInt, PositiveInt
from pydantic_settings import BaseSettings

from .constants import PoolDefaults


class PoolSettings(BaseSettings):
    MAX_SIZE: PositiveInt | None = Field(
        default=PoolDefaults.MAX_SIZE,
        description="Maximum number of connections in the pool",
        le=1000,
    )
    MIN_SIZE: NonNegativeInt | None = Field(
        default=PoolDefaults.MIN_SIZE,
        description="Minimum number of connections in the pool",
        le=999,
    )
    MAX_IDLE_TIME_MS: NonNegativeInt | None = Field(
        default=PoolDefaults.MAX_IDLE_TIME_MS,
        description="Maximum idle time for a connection (ms), None disables "
        "limit",
    )
    MAX_CONNECTING: PositiveInt | None = Field(
        default=PoolDefaults.MAX_CONNECTING,
        description="Maximum number of concurrent connection attempts",
        le=100,
    )
    WAIT_QUEUE_TIMEOUT_MS: NonNegativeInt | None = Field(
        default=PoolDefaults.WAIT_QUEUE_TIMEOUT_MS,
        description="Max time to wait for a free connection in the pool (ms)",
    )
    HEARTBEAT_FREQUENCY_MS: NonNegativeInt | None = Field(
        default=PoolDefaults.HEARTBEAT_FREQUENCY_MS,
        description="Interval between server monitoring checks (ms)",
    )
    SERVER_MONITORING_MODE: str | None = Field(
        default=PoolDefaults.SERVER_MONITORING_MODE,
        description="Server monitoring mode: auto, stream, poll",
        pattern="^(auto|stream|poll)$",
    )

    @property
    def client_kwargs(self) -> dict[str, Any]:
        """Returns a dictionary with parameters for creating an AsyncMongoClient
        instance.
        """
        result: dict[str, Any] = {}

        if self.MAX_SIZE is not None:
            result["maxPoolSize"] = self.MAX_SIZE
        if self.MIN_SIZE is not None:
            result["minPoolSize"] = self.MIN_SIZE
        if self.MAX_IDLE_TIME_MS is not None:
            result["maxIdleTimeMS"] = self.MAX_IDLE_TIME_MS
        if self.MAX_CONNECTING is not None:
            result["maxConnecting"] = self.MAX_CONNECTING
        if self.WAIT_QUEUE_TIMEOUT_MS is not None:
            result["waitQueueTimeoutMS"] = self.WAIT_QUEUE_TIMEOUT_MS
        if self.HEARTBEAT_FREQUENCY_MS is not None:
            result["heartbeatFrequencyMS"] = self.HEARTBEAT_FREQUENCY_MS
        if self.SERVER_MONITORING_MODE is not None:
            result["serverMonitoringMode"] = self.SERVER_MONITORING_MODE

        return result
