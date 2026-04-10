from enum import StrEnum
from typing import Final, final


class ConnectionSchemaEnum(StrEnum):
    mongodb = "mongodb"
    mongodb_srv = "mongodb+srv"


@final
class ConnectionDefaults:
    HOST: Final[str] = "localhost"
    PORT: Final[int] = 27017
    USERNAME: Final[str] = ""
    PASSWORD: Final[str] = ""
    SCHEMA: Final[ConnectionSchemaEnum] = ConnectionSchemaEnum.mongodb
    DATABASE: Final[str] = "default-database"
