import logging
from typing import Any

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

from src.infrastructure.database.mongo.logger import LoggerNames

from .authentication import AuthenticationSettings
from .compression import CompressionSettings
from .connection import ConnectionSettings
from .connection_mode import ConnectionModeSettings
from .constants import BaseDefaults
from .erro_handling import ErrorHandlingSettings
from .pool import PoolSettings
from .read_concern import ReadConcernSettings
from .representation import RepresentationSettings
from .retry_behavior import RetryBehaviorSettings
from .srv import SRVSettings
from .timeouts import TimeoutsSettings
from .tls import TLSSettings
from .write_concern import WriteConcernSettings

logger = logging.getLogger(LoggerNames.init())


class Settings(BaseSettings):
    model_config = SettingsConfigDict(**BaseDefaults.model_config())

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # noqa: ANN401
        logger.info("loading the settings...")
        super().__init__(*args, **kwargs)
        logger.info("settings was loaded successfully")
        logger.debug(f"settings parameters: {self._parameters()}")

    def _parameters(self) -> dict[str, Any]:
        config = self.client_kwargs
        config.update({"database": self.database})
        config.update({"connection": self.connection.dsn().encoded_string()})
        return config

    DB_NAME: str = Field(
        default=BaseDefaults.DB_NAME,
        description="Database name",
        min_length=1,
        max_length=32,
    )

    connection: ConnectionSettings = ConnectionSettings()
    pool: PoolSettings = PoolSettings()
    timeouts: TimeoutsSettings = TimeoutsSettings()
    retry_behavior: RetryBehaviorSettings = RetryBehaviorSettings()
    tls: TLSSettings = TLSSettings()
    compression: CompressionSettings = CompressionSettings()
    representation: RepresentationSettings = RepresentationSettings()
    connection_mode: ConnectionModeSettings = ConnectionModeSettings()
    authentication: AuthenticationSettings = AuthenticationSettings()
    write_concern: WriteConcernSettings = WriteConcernSettings()
    read_concern: ReadConcernSettings = ReadConcernSettings()
    srv: SRVSettings = SRVSettings()
    error_handling: ErrorHandlingSettings = ErrorHandlingSettings()

    @property
    def database(self) -> str:
        """Returns the name of the MongoDB database"""
        return self.DB_NAME

    @property
    def connection_string(self) -> str:
        """Returns the MongoDB connection string"""
        return self.connection.dsn(with_secret=True).encoded_string()

    @property
    def client_kwargs(self) -> dict[str, Any]:
        """Returns a dictionary with parameters for creating an AsyncMongoClient
        instance.
        """
        d: dict[str, Any] = {}

        d.update(self.pool.client_kwargs)
        d.update(self.timeouts.client_kwargs)
        d.update(self.retry_behavior.client_kwargs)
        d.update(self.tls.client_kwargs)
        d.update(self.compression.client_kwargs)
        d.update(self.representation.client_kwargs)
        d.update(self.connection_mode.client_kwargs)
        d.update(self.write_concern.client_kwargs)
        d.update(self.read_concern.client_kwargs)
        d.update(self.error_handling.client_kwargs)

        if self.connection.use_authentication:
            d.update(self.authentication.client_kwargs)
        if self.connection.use_srv:
            d.update(self.srv.client_kwargs)

        return d
