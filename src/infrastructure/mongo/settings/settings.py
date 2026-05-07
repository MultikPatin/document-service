from pydantic import Field, MongoDsn, PositiveInt, SecretStr
from pydantic_settings import BaseSettings

from src.domain.utils import settings_model_config
from src.infrastructure.mongo.annotations import ClientKwargsType
from src.infrastructure.mongo.constants import ENV_PREFIX
from src.infrastructure.mongo.constants.settings import BaseDefaults, SchemaEnum

from .authentication import AuthenticationSettings
from .compression import CompressionSettings
from .connection import ConnectionSettings
from .error_handling import ErrorHandlingSettings
from .pool import PoolSettings
from .read import ReadSettings
from .representation import RepresentationSettings
from .retry import RetrySettings
from .srv import SRVSettings
from .timeouts import TimeoutsSettings
from .tls import TLSSettings
from .write import WriteSettings


class Settings(BaseSettings):
    model_config = settings_model_config(env_prefix=ENV_PREFIX)

    DB_NAME: str = Field(
        default=BaseDefaults.DB_NAME,
        description="Database name",
        min_length=1,
        max_length=32,
    )
    HOST: str = Field(
        default=BaseDefaults.HOST,
        description="Host address",
        min_length=1,
        max_length=255,
    )
    PORT: PositiveInt = Field(
        default=BaseDefaults.PORT,
        description="Port number",
        lt=65536,
    )
    USERNAME: str = Field(
        default=BaseDefaults.USERNAME,
        description="Authentication username",
        max_length=255,
    )
    PASSWORD: SecretStr = Field(
        default=SecretStr(BaseDefaults.PASSWORD),
        description="Authentication password",
        max_length=255,
    )
    SCHEMA: SchemaEnum = Field(
        default=SchemaEnum.mongodb,
        description="Connection scheme: mongodb or mongodb+srv",
    )

    pool: PoolSettings = PoolSettings()
    timeouts: TimeoutsSettings = TimeoutsSettings()
    retry: RetrySettings = RetrySettings()
    tls: TLSSettings = TLSSettings()
    compression: CompressionSettings = CompressionSettings()
    representation: RepresentationSettings = RepresentationSettings()
    connection: ConnectionSettings = ConnectionSettings()
    authentication: AuthenticationSettings = AuthenticationSettings()
    write: WriteSettings = WriteSettings()
    read: ReadSettings = ReadSettings()
    srv: SRVSettings = SRVSettings()
    error_handling: ErrorHandlingSettings = ErrorHandlingSettings()

    @property
    def database(self) -> str:
        """Returns the name of the MongoDB database"""
        return self.DB_NAME

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

    @property
    def use_srv(self) -> bool:
        return SchemaEnum.mongodb_srv == self.SCHEMA

    @property
    def use_authentication(self) -> bool:
        return bool(self.USERNAME)

    @property
    def connection_string(self) -> str:
        """Returns the MongoDB connection string"""
        return self.dsn(with_secret=True).encoded_string()

    @property
    def client_kwargs(self) -> ClientKwargsType:
        """Returns a dictionary with parameters for creating an AsyncMongoClient
        instance.
        """
        d: ClientKwargsType = {}

        d.update(self.pool.client_kwargs)
        d.update(self.timeouts.client_kwargs)
        d.update(self.retry.client_kwargs)
        d.update(self.tls.client_kwargs)
        d.update(self.compression.client_kwargs)
        d.update(self.representation.client_kwargs)
        d.update(self.connection.client_kwargs)
        d.update(self.write.client_kwargs)
        d.update(self.read.client_kwargs)
        d.update(self.error_handling.client_kwargs)

        if self.use_authentication:
            d.update(self.authentication.client_kwargs)
        if self.use_srv:
            d.update(self.srv.client_kwargs)

        return d
