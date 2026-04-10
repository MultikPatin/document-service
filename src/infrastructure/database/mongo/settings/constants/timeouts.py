from typing import Final, final


@final
class TimeoutsDefaults:
    CONNECTION_MS: Final[int] = 20000
    SOCKET_MS: Final[int] = 20000
    SERVER_SELECTION_MS: Final[int] = 30000
    OPERATION_MS: Final[int] = 10000


@final
class TimeoutsKeys:
    CONNECTION: Final[str] = "connectTimeoutMS"
    SOCKET: Final[str] = "socketTimeoutMS"
    SERVER_SELECTION: Final[str] = "serverSelectionTimeoutMS"
    OPERATION: Final[str] = "timeoutMS"
