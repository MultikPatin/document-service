import logging
from collections.abc import Sequence
from typing import Any

from pydantic import Field, MongoDsn, NonNegativeInt, PositiveInt, SecretStr
from pydantic_settings import BaseSettings

from src.core.settings import model_config

from .constants import Defaults, LoggerNames

logger = logging.getLogger(LoggerNames.init())


class Settings(BaseSettings):
    model_config = model_config(env_prefix=Defaults.ENV_PREFIX)

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # noqa: ANN401
        logger.info("loading the settings...")
        super().__init__(*args, **kwargs)
        logger.info("settings was loaded successfully")
        logger.debug(f"settings parameters: {self._config()}")

    def _config(self) -> dict[str, Any]:
        config = {"connections": self.get_connections()}
        config.update(self.client_kwargs)
        return config

    # Connection basics
    HOST: str = Field(
        default=Defaults.HOST,
        description="Host address",
        min_length=1,
        max_length=255,
    )
    PORT: PositiveInt = Field(
        default=Defaults.PORT,
        description="Port number",
        lt=65536,
    )
    USERNAME: str = Field(
        default=Defaults.USERNAME,
        description="Authentication username",
        max_length=255,
    )
    PASSWORD: SecretStr = Field(
        default=Defaults.PASSWORD,
        description="Authentication password",
        max_length=255,
    )
    SCHEMA: str = Field(
        default=Defaults.SCHEMA,
        description="Connection scheme: mongodb or mongodb+srv",
        pattern="^mongodb(?:\\+srv)?$",
    )
    DATABASE: str = Field(
        default=Defaults.DATABASE,
        description="Default database name",
        min_length=1,
        max_length=32,
    )

    # Pool settings
    MAX_POOL_SIZE: PositiveInt | None = Field(
        default=Defaults.MAX_POOL_SIZE,
        description="Maximum number of connections in the pool",
        le=1000,
    )
    MIN_POOL_SIZE: NonNegativeInt | None = Field(
        default=Defaults.MIN_POOL_SIZE,
        description="Minimum number of connections in the pool",
        le=1000,
    )
    MAX_IDLE_TIME_MS: NonNegativeInt | None = Field(
        default=Defaults.MAX_IDLE_TIME_MS,
        description="Maximum idle time for a connection (ms), None disables "
        "limit",
    )
    MAX_CONNECTING: PositiveInt | None = Field(
        default=Defaults.MAX_CONNECTING,
        description="Maximum number of concurrent connection attempts",
        le=100,
    )
    WAIT_QUEUE_TIMEOUT_MS: NonNegativeInt | None = Field(
        default=Defaults.WAIT_QUEUE_TIMEOUT_MS,
        description="Max time to wait for a free connection in the pool (ms)",
    )
    HEARTBEAT_FREQUENCY_MS: NonNegativeInt | None = Field(
        default=Defaults.HEARTBEAT_FREQUENCY_MS,
        description="Interval between server monitoring checks (ms)",
    )
    SERVER_MONITORING_MODE: str | None = Field(
        default=Defaults.SERVER_MONITORING_MODE,
        description="Server monitoring mode: auto, stream, poll",
        pattern="^(auto|stream|poll)$",
    )

    # Timeouts
    CONNECT_TIMEOUT_MS: NonNegativeInt = Field(
        default=Defaults.CONNECT_TIMEOUT_MS,
        description="Connect timeout (ms)",
    )
    SOCKET_TIMEOUT_MS: NonNegativeInt = Field(
        default=Defaults.SOCKET_TIMEOUT_MS,
        description="Socket timeout (ms)",
    )
    SERVER_SELECTION_TIMEOUT_MS: NonNegativeInt = Field(
        default=Defaults.SERVER_SELECTION_TIMEOUT_MS,
        description="Server selection timeout (ms)",
    )
    TIMEOUT_MS: NonNegativeInt | None = Field(
        default=Defaults.TIMEOUT_MS,
        description="Operation timeout (ms), None means no timeout",
    )

    # Retry behavior
    RETRY_WRITES: bool = Field(
        default=Defaults.RETRY_WRITES,
        description="Enable retryable writes",
    )
    RETRY_READS: bool = Field(
        default=Defaults.RETRY_READS,
        description="Enable retryable reads",
    )

    # TLS/SSL
    TLS: bool = Field(
        default=Defaults.TLS,
        description="Enable TLS encryption",
    )
    TLS_INSECURE: bool = Field(
        default=Defaults.TLS_INSECURE,
        description="Specify whether TLS constraints should "
        "be relaxed as much as possible",
    )
    TLS_ALLOW_INVALID_CERTIFICATES: bool = Field(
        default=Defaults.TLS_ALLOW_INVALID_CERTIFICATES,
        description="Allow invalid TLS certificates",
    )
    TLS_ALLOW_INVALID_HOSTNAMES: bool = Field(
        default=Defaults.TLS_ALLOW_INVALID_HOSTNAMES,
        description="Allow mismatched TLS certificate hostnames",
    )
    TLS_CA_FILE: str | None = Field(
        default=Defaults.TLS_CA_FILE,
        description="Path to custom CA file for TLS validation",
        min_length=1,
    )
    TLS_CERTIFICATE_KEY_FILE: str | None = Field(
        default=Defaults.TLS_CERTIFICATE_KEY_FILE,
        description="Path to client certificate and key file",
        min_length=1,
    )
    TLS_CRL_FILE: str | None = Field(
        default=Defaults.TLS_CRL_FILE,
        description="Path to file containing a PEM or DER "
        "formatted certificate revocation list",
        min_length=1,
    )
    TLS_CERTIFICATE_KEY_FILE_PASSWORD: str | None = Field(
        default=Defaults.TLS_CERTIFICATE_KEY_FILE_PASSWORD,
        description="The password or passphrase for "
        "decrypting the private key in ``tlsCertificateKeyFile``. "
        "Only necessary if the private key is encrypted",
        min_length=1,
    )
    TLS_DISABLE_OCSP_ENDPOINT_CHECK: bool = Field(
        default=Defaults.TLS_DISABLE_OCSP_ENDPOINT_CHECK,
        description="If ``True``, disables certificate revocation status "
        "checking via the OCSP responder specified on "
        "the server certificate",
    )

    # Compression
    COMPRESSORS: str | None = Field(
        default=Defaults.COMPRESSORS,
        description="Compression method: snappy, zlib, zstd",
        pattern="^(snappy|zlib|zstd)?$",
    )
    ZLIB_COMPRESSION_LEVEL: NonNegativeInt | None = Field(
        default=Defaults.ZLIB_COMPRESSION_LEVEL,
        description="zlib compression level (0-9)",
        le=9,
    )

    # UUID representation
    UUID_REPRESENTATION: str = Field(
        default=Defaults.UUID_REPRESENTATION,
        description="UUID representation format",
        pattern="^(standard|pythonLegacy|javaLegacy|csharpLegacy|unspecified)$",
    )

    # Connection mode
    DIRECT_CONNECTION: bool | None = Field(
        default=Defaults.DIRECT_CONNECTION,
        description="Direct connection to single server",
    )
    APPNAME: str | None = Field(
        default=Defaults.APPNAME,
        description="Application name (visible in logs)",
        max_length=128,
    )
    READ_PREFERENCE: str | None = Field(
        default=Defaults.READ_PREFERENCE,
        description="Read preference mode",
        pattern="^(primary|primaryPreferred|secondary|secondaryPreferred|nearest)?$",
    )
    READ_PREFERENCE_TAGS: str | None = Field(
        default=Defaults.READ_PREFERENCE_TAGS,
        description="Specifies a tag set as a comma-separated list "
        "of colon-separated key-value pairs",
    )
    MAX_STALENESS_SECONDS: NonNegativeInt | None = Field(
        default=Defaults.MAX_STALENESS_SECONDS,
        description="The maximum estimated length of time a replica set "
        "secondary can fall behind the primary in replication "
        "before it will no longer be selected for operations",
        le=90000,
    )
    REPLICA_SET_NAME: str | None = Field(
        default=Defaults.REPLICA_SET_NAME,
        description="Replica set name",
        min_length=1,
        max_length=128,
    )

    # Authentication
    AUTH_SOURCE: str = Field(
        default=Defaults.AUTH_SOURCE,
        description="Database to authenticate against",
        min_length=1,
        max_length=64,
    )
    AUTH_MECHANISM: str = Field(
        default=Defaults.AUTH_MECHANISM,
        description="Authentication mechanism",
        pattern="^(SCRAM-SHA-1|SCRAM-SHA-256)$",
    )
    # AUTH_MECHANISM_PROPERTIES: str | None = Field(
    #     default=Defaults.AUTH_MECHANISM_PROPERTIES,
    #     description="Authentication mechanism",
    #     pattern="^(SCRAM-SHA-1|SCRAM-SHA-256)$",
    # )

    # Write concern
    WRITE_CONCERN_W: int | str | None = Field(
        default=Defaults.WRITE_CONCERN_W,
        description="Write concern: number of replicas or 'majority'",
    )
    JOURNAL: bool = Field(
        default=Defaults.JOURNAL,
        description="Wait for write to be written to journal",
    )
    FSYNC: bool = Field(
        default=Defaults.FSYNC,
        description="Force the write operation to fsync to disk",
    )

    # Read concern
    READ_CONCERN_LEVEL: str = Field(
        default=Defaults.READ_CONCERN_LEVEL,
        description="Read concern level: local, majority, linearizable",
        pattern="^(local|majority|linearizable)?$",
    )

    # SRV & API
    SRV_SERVICE_NAME: str = Field(
        default=Defaults.SRV_SERVICE_NAME,
        description="Service name for DNS SRV lookups",
        min_length=1,
    )
    SRV_MAX_HOSTS: PositiveInt = Field(
        default=Defaults.SRV_MAX_HOSTS,
        description="Maximum number of hosts to connect to with SRV",
    )

    # Unicode error handling
    UNICODE_DECODE_ERROR_HANDLER: str = Field(
        default=Defaults.UNICODE_DECODE_ERROR_HANDLER,
        description="Handler for Unicode decode errors: "
        "strict, ignore, replace",
        pattern="^(strict|ignore|replace|backslashreplace|surrogateescape)$",
    )

    @property
    def database(self) -> str:
        """Returns the name of the MongoDB database"""
        return self.DATABASE

    def _dsn(self, with_secret: bool = False) -> MongoDsn:
        """Generate MongoDB DSN with pre-built query parameters."""
        return MongoDsn.build(
            host=self.HOST,
            port=self.PORT,
            scheme=self.SCHEMA,
            username=self.USERNAME,
            password=self.PASSWORD.get_secret_value()
            if with_secret
            else str(self.PASSWORD),
        )

    def get_connections(self, with_secret: bool = False) -> str | Sequence[str]:
        """It can also be a list of connections but no more than one URI"""
        return self._dsn(with_secret).unicode_string()

    @property
    def client_kwargs(self) -> dict[str, Any]:
        """Returns a dictionary with parameters for creating an AsyncMongoClient
        instance.
        """
        result: dict[str, Any] = {}

        self._pool_setting(result)
        self._timeouts_setting(result)
        self._retry_behavior(result)
        self._tls_setting(result)
        self._compression_setting(result)
        self._uuid_representation_setting(result)
        self._connection_mode_setting(result)
        self._authentication_setting(result)
        self._write_concern_setting(result)
        self._read_concern_setting(result)
        self._srv_api_setting(result)
        self._unicode_error_handling_setting(result)

        return result

    def _pool_setting(self, result: dict[str, Any]) -> None:
        if self.MAX_POOL_SIZE:
            result["maxPoolSize"] = self.MAX_POOL_SIZE
        if self.MIN_POOL_SIZE:
            result["minPoolSize"] = self.MIN_POOL_SIZE
        if self.MAX_IDLE_TIME_MS:
            result["maxIdleTimeMS"] = self.MAX_IDLE_TIME_MS
        if self.MAX_CONNECTING:
            result["maxConnecting"] = self.MAX_CONNECTING
        if self.HEARTBEAT_FREQUENCY_MS:
            result["heartbeatFrequencyMS"] = self.HEARTBEAT_FREQUENCY_MS
        if self.SERVER_MONITORING_MODE:
            result["serverMonitoringMode"] = self.SERVER_MONITORING_MODE

    def _timeouts_setting(self, result: dict[str, Any]) -> None:
        result["socketTimeoutMS"] = self.SOCKET_TIMEOUT_MS
        result["connectTimeoutMS"] = self.CONNECT_TIMEOUT_MS
        result["serverSelectionTimeoutMS"] = self.SERVER_SELECTION_TIMEOUT_MS

        if self.TIMEOUT_MS:
            result["timeoutMS"] = self.TIMEOUT_MS
        if self.WAIT_QUEUE_TIMEOUT_MS:
            result["waitQueueTimeoutMS"] = self.WAIT_QUEUE_TIMEOUT_MS

    def _retry_behavior(self, result: dict[str, Any]) -> None:
        result["retryWrites"] = self.RETRY_WRITES
        result["retryReads"] = self.RETRY_READS

    def _tls_setting(self, result: dict[str, Any]) -> None:
        if self.TLS:
            result["tls"] = self.TLS
            result["tlsInsecure"] = self.TLS_INSECURE
            result["tlsAllowInvalidCertificates"] = (
                self.TLS_ALLOW_INVALID_CERTIFICATES
            )
            result["tlsAllowInvalidHostnames"] = (
                self.TLS_ALLOW_INVALID_HOSTNAMES
            )
            result["tlsDisableOCSPEndpointCheck"] = (
                self.TLS_DISABLE_OCSP_ENDPOINT_CHECK
            )

            if self.TLS_CA_FILE:
                result["tlsCAFile"] = self.TLS_CA_FILE
            if self.TLS_CERTIFICATE_KEY_FILE:
                result["tlsCertificateKeyFile"] = self.TLS_CERTIFICATE_KEY_FILE
            if self.TLS_CRL_FILE:
                result["tlsCRLFile"] = self.TLS_CRL_FILE
            if self.TLS_CERTIFICATE_KEY_FILE_PASSWORD:
                result["tlsCertificateKeyFilePassword"] = (
                    self.TLS_CERTIFICATE_KEY_FILE_PASSWORD
                )

    def _compression_setting(self, result: dict[str, Any]) -> None:
        if self.COMPRESSORS:
            result["compressors"] = self.COMPRESSORS
        if self.ZLIB_COMPRESSION_LEVEL:
            result["zlibCompressionLevel"] = self.ZLIB_COMPRESSION_LEVEL

    def _uuid_representation_setting(self, result: dict[str, Any]) -> None:
        result["uuidRepresentation"] = self.UUID_REPRESENTATION

    def _connection_mode_setting(self, result: dict[str, Any]) -> None:
        if self.APPNAME:
            result["appname"] = self.APPNAME
        if self.DIRECT_CONNECTION:
            result["directConnection"] = self.DIRECT_CONNECTION
        if self.READ_PREFERENCE:
            result["readPreference"] = self.READ_PREFERENCE
        if self.READ_PREFERENCE_TAGS:
            result["readPreferenceTags"] = self.READ_PREFERENCE_TAGS
        if self.MAX_STALENESS_SECONDS:
            result["maxStalenessSeconds"] = self.MAX_STALENESS_SECONDS
        if self.REPLICA_SET_NAME:
            result["replicaSet"] = self.REPLICA_SET_NAME

    def _authentication_setting(self, result: dict[str, Any]) -> None:
        if self.USERNAME:
            result["authSource"] = self.AUTH_SOURCE
            result["authMechanism"] = self.AUTH_MECHANISM
            # result["authMechanismProperties"] = self.AUTH_MECHANISM_PROPERTIES

    def _write_concern_setting(self, result: dict[str, Any]) -> None:
        result["journal"] = self.JOURNAL
        result["fsync"] = self.FSYNC

        if self.WRITE_CONCERN_W:
            result["w"] = self.WRITE_CONCERN_W

    def _read_concern_setting(self, result: dict[str, Any]) -> None:
        result["readConcernLevel"] = self.READ_CONCERN_LEVEL

    def _srv_api_setting(self, result: dict[str, Any]) -> None:
        if self.SCHEMA.endswith("srv"):
            result["srvServiceName"] = self.SRV_SERVICE_NAME
            result["srvMaxHosts"] = self.SRV_MAX_HOSTS

    def _unicode_error_handling_setting(self, result: dict[str, Any]) -> None:
        result["unicode_decode_error_handler"] = (
            self.UNICODE_DECODE_ERROR_HANDLER
        )
