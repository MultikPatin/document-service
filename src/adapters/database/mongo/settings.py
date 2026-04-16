from logging import Logger
from typing import Any

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
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(**BaseDefaults.model_config())

    def __init__(
        self,
        *args: Any,  # noqa: ANN401
        logger: Logger | None = None,
        **kwargs: Any,  # noqa: ANN401
    ) -> None:
        if logger is None:
            super().__init__(*args, **kwargs)
        else:
            logger.info("loading the settings...")
            super().__init__(*args, **kwargs)
            logger.info("settings was loaded successfully")
            logger.debug(f"settings parameters: {self._parameters()}")

    def _parameters(self) -> dict[str, Any]:
        p = self.client_kwargs
        p.update({"database": self.database})
        p.update({"connection": self.connection.dsn().encoded_string()})
        return p

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
        return self.connection.DB_NAME

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
