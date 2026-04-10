from enum import StrEnum
from typing import Final, final


class AuthenticationMechanismEnum(StrEnum):
    SCRAM_SHA_1 = "SCRAM-SHA-1"
    SCRAM_SHA_256 = "SCRAM-SHA-256"


@final
class AuthenticationDefaults:
    SOURCE: Final[str] = "admin"
    MECHANISM: Final[AuthenticationMechanismEnum] = (
        AuthenticationMechanismEnum.SCRAM_SHA_256
    )
    MECHANISM_PROPERTIES: Final[str | None] = None


@final
class AuthenticationKeys:
    SOURCE: Final[str] = "authSource"
    MECHANISM: Final[str] = "authMechanism"
    MECHANISM_PROPERTIES: Final[str] = "authMechanismProperties"
