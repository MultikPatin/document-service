from typing import Final, final


@final
class TimeoutsDefaults:
    CONNECTION: Final[int] = 20000
    SOCKET: Final[int] = 20000
    SERVER_SELECTION: Final[int] = 30000
    OPERATION: Final[int] = 10000


@final
class TimeoutsKeys:
    CONNECTION: Final[str] = "connectTimeoutMS"
    SOCKET: Final[str] = "socketTimeoutMS"
    SERVER_SELECTION: Final[str] = "serverSelectionTimeoutMS"
    OPERATION: Final[str] = "timeoutMS"
