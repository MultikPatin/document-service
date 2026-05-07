from enum import StrEnum
from typing import Final, final


class SchemaEnum(StrEnum):
    mongodb = "mongodb"
    mongodb_srv = "mongodb+srv"


@final
class BaseDefaults:
    DB_NAME: Final[str] = "default-db"
    HOST: Final[str] = "localhost"
    PORT: Final[int] = 27017
    USERNAME: Final[str] = ""
    PASSWORD: Final[str] = ""
    SCHEMA: Final[SchemaEnum] = SchemaEnum.mongodb
    DATABASE: Final[str] = "default-database"
