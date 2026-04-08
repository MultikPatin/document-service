import logging
from collections.abc import Sequence
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
    model_config = SettingsConfigDict(
        env_file=BaseDefaults.ENV_FILE,
        env_prefix=BaseDefaults.ENV_PREFIX,
        env_file_encoding=BaseDefaults.ENV_FILE_ENCODING,
        env_nested_delimiter=BaseDefaults.ENV_NESTED_DELIMITER,
        extra=BaseDefaults.EXTRA,
        frozen=BaseDefaults.FROZEN,
    )

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # noqa: ANN401
        logger.info("loading the settings...")
        super().__init__(*args, **kwargs)
        logger.info("settings was loaded successfully")
        logger.debug(f"settings parameters: {self._parameters()}")

    def _parameters(self) -> dict[str, Any]:
        config = self.client_kwargs
        config.update({"database": self.database})
        config.update({"connections": self.get_connections()})
        return config

    DB_NAME: str = Field(
        default=BaseDefaults.DB_NAME,
        description="Database name",
        min_length=1,
        max_length=32,
    )

    connection0: ConnectionSettings = ConnectionSettings()

    @property
    def database(self) -> str:
        """Returns the name of the MongoDB database"""
        return self.DB_NAME

    def get_connections(self, with_secret: bool = False) -> Sequence[str]:
        """It can also be a list of connections but no more than one URI"""
        dsn = self.connection0.dsn(with_secret=with_secret)
        return [dsn.encoded_string()]

    @property
    def client_kwargs(self) -> dict[str, Any]:
        """Returns a dictionary with parameters for creating an AsyncMongoClient
        instance.
        """
        result: dict[str, Any] = {}

        result.update(self.pool.client_kwargs)
        result.update(self.timeouts.client_kwargs)
        result.update(self.retry_behavior.client_kwargs)
        result.update(self.tls.client_kwargs)
        result.update(self.compression.client_kwargs)
        result.update(self.representation.client_kwargs)
        result.update(self.connection_mode.client_kwargs)
        result.update(self.write_concern.client_kwargs)
        result.update(self.read_concern.client_kwargs)
        result.update(self.error_handling.client_kwargs)

        # Fix for more than 1 connection
        if self.connection0.USERNAME:
            result.update(self.authentication.client_kwargs)
        if self.connection0.SCHEMA.endswith("srv"):
            result.update(self.srv.client_kwargs)

        return result

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
