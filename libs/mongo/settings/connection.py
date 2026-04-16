from pydantic import Field, MongoDsn, PositiveInt, SecretStr
from pydantic_settings import BaseSettings

from libs.mongo.constants.settings import (
    ConnectionDefaults,
    ConnectionSchemaEnum,
)


class ConnectionSettings(BaseSettings):
    DB_NAME: str = Field(
        default=ConnectionDefaults.DB_NAME,
        description="Database name",
        min_length=1,
        max_length=32,
    )
    HOST: str = Field(
        default=ConnectionDefaults.HOST,
        description="Host address",
        min_length=1,
        max_length=255,
    )
    PORT: PositiveInt = Field(
        default=ConnectionDefaults.PORT,
        description="Port number",
        lt=65536,
    )
    USERNAME: str = Field(
        default=ConnectionDefaults.USERNAME,
        description="Authentication username",
        max_length=255,
    )
    PASSWORD: SecretStr = Field(
        default=SecretStr(ConnectionDefaults.PASSWORD),
        description="Authentication password",
        max_length=255,
    )
    SCHEMA: ConnectionSchemaEnum = Field(
        default=ConnectionSchemaEnum.mongodb,
        description="Connection scheme: mongodb or mongodb+srv",
    )

    @property
    def use_srv(self) -> bool:
        return ConnectionSchemaEnum.mongodb_srv == self.SCHEMA

    @property
    def use_authentication(self) -> bool:
        return bool(self.USERNAME)

    def dsn(self, with_secret: bool = False) -> MongoDsn:
        """Generate MongoDB DSN with pre-built query parameters."""
        return MongoDsn.build(
            host=self.HOST,
            port=self.PORT,
            scheme=self.SCHEMA.value,
            username=self.USERNAME,
            password=self.PASSWORD.get_secret_value()
            if with_secret
            else str(self.PASSWORD),
        )
