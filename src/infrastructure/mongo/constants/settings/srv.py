from typing import Final, final


@final
class SRVDefaults:
    SERVICE_NAME: Final[str] = "mongodb"
    MAX_HOSTS: Final[int] = 1


@final
class SRVKeys:
    SERVICE_NAME: Final[str] = "srvServiceName"
    MAX_HOSTS: Final[str] = "srvMaxHosts"
