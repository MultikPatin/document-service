from logging import Logger
from typing import Any

from pydantic_settings import SettingsConfigDict

from libs.mongo.constants.settings import BaseDefaults
from libs.mongo.settings import (
    AuthenticationSettings,
    CompressionSettings,
    ConnectionModeSettings,
    ConnectionSettings,
    ErrorHandlingSettings,
    PoolSettings,
    ReadConcernSettings,
    RepresentationSettings,
    RetryBehaviorSettings,
    SRVSettings,
    TimeoutsSettings,
    TLSSettings,
    WriteConcernSettings,
)


class Settings(ConnectionSettings):
    model_config = SettingsConfigDict(**BaseDefaults.model_config())

    def __init__(self, logger: Logger | None = None) -> None:
        if logger is None:
            super().__init__()
        else:
            logger.info("loading the settings...")
            super().__init__()
            logger.info("settings was loaded successfully")
            logger.debug(f"settings parameters: {self._parameters()}")

    def _parameters(self) -> dict[str, Any]:
        p = self.client_kwargs
        p.update({"database": self.database})
        p.update({"connection": self.dsn().encoded_string()})
        return p

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
        return self.dsn(with_secret=True).encoded_string()

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

        if self.use_authentication:
            d.update(self.authentication.client_kwargs)
        if self.use_srv:
            d.update(self.srv.client_kwargs)

        return d
