from enum import StrEnum
from typing import Final, final


class ReadConcernLevelEnum(StrEnum):
    local = "local"
    majority = "majority"
    linearizable = "linearizable"


@final
class ReadConcernDefaults:
    LEVEL: Final[ReadConcernLevelEnum] = ReadConcernLevelEnum.majority


@final
class ReadConcernKeys:
    LEVEL: Final[str] = "readConcernLevel"
