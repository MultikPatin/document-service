from enum import StrEnum
from typing import Final, final


class PoolServerMonitoringModEenum(StrEnum):
    auto = "auto"
    stream = "stream"
    poll = "poll"


@final
class PoolDefaults:
    MAX_SIZE: Final[int] = 100
    MIN_SIZE: Final[int] = 0
    MAX_IDLE_TIME: Final[int | None] = None
    MAX_CONNECTING: Final[int | None] = None
    WAIT_QUEUE_TIMEOUT: Final[int | None] = None
    HEARTBEAT_FREQUENCY: Final[int] = 10000
    SERVER_MONITORING_MODE: Final[PoolServerMonitoringModEenum | None] = (
        PoolServerMonitoringModEenum.auto
    )


@final
class PoolKeys:
    MAX_SIZE = "maxPoolSize"
    MIN_SIZE = "minPoolSize"
    MAX_IDLE_TIME = "maxIdleTimeMS"
    MAX_CONNECTING = "maxConnecting"
    WAIT_QUEUE_TIMEOUT = "waitQueueTimeoutMS"
    HEARTBEAT_FREQUENCY = "heartbeatFrequencyMS"
    SERVER_MONITORING_MODE = "serverMonitoringMode"
