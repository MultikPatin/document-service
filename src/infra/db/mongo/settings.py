from typing import Any

from pydantic import Field, MongoDsn, NonNegativeInt, PositiveInt, SecretStr
from pydantic_settings import BaseSettings

from src.core.settings import Defaults, model_config
from src.infra.db.mongo.constants import _MongoDefaults


class _Settings(BaseSettings):
    model_config = model_config(env_prefix=_MongoDefaults.ENV_PREFIX)

    # Connection basics
    HOST: str = Field(
        default=Defaults.HOST,
        description="MongoDB server host address",
        min_length=1,
        max_length=255,
    )
    PORT: PositiveInt = Field(
        default=_MongoDefaults.PORT,
        description="MongoDB server port number",
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
        default=_MongoDefaults.SCHEMA,
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
        default=_MongoDefaults.MAX_POOL_SIZE,
        description="Maximum number of connections in the pool",
        le=1000,
    )
    MIN_POOL_SIZE: NonNegativeInt | None = Field(
        default=_MongoDefaults.MIN_POOL_SIZE,
        description="Minimum number of connections in the pool",
        le=1000,
    )
    MAX_IDLE_TIME_MS: NonNegativeInt | None = Field(
        default=_MongoDefaults.MAX_IDLE_TIME_MS,
        description="Maximum idle time for a connection (ms), None disables "
        "limit",
    )
    MAX_CONNECTING: PositiveInt | None = Field(
        default=_MongoDefaults.MAX_CONNECTING,
        description="Maximum number of concurrent connection attempts",
        le=100,
    )
    WAIT_QUEUE_TIMEOUT_MS: NonNegativeInt | None = Field(
        default=_MongoDefaults.WAIT_QUEUE_TIMEOUT_MS,
        description="Max time to wait for a free connection in the pool (ms)",
    )
    HEARTBEAT_FREQUENCY_MS: NonNegativeInt | None = Field(
        default=_MongoDefaults.HEARTBEAT_FREQUENCY_MS,
        description="Interval between server monitoring checks (ms)",
    )
    SERVER_MONITORING_MODE: str | None = Field(
        default=_MongoDefaults.SERVER_MONITORING_MODE,
        description="Server monitoring mode: auto, stream, poll",
        pattern="^(auto|stream|poll)$",
    )

    # Timeouts
    CONNECT_TIMEOUT_MS: NonNegativeInt = Field(
        default=_MongoDefaults.CONNECT_TIMEOUT_MS,
        description="Connect timeout (ms)",
    )
    SOCKET_TIMEOUT_MS: NonNegativeInt = Field(
        default=_MongoDefaults.SOCKET_TIMEOUT_MS,
        description="Socket timeout (ms)",
    )
    SERVER_SELECTION_TIMEOUT_MS: NonNegativeInt = Field(
        default=_MongoDefaults.SERVER_SELECTION_TIMEOUT_MS,
        description="Server selection timeout (ms)",
    )
    TIMEOUT_MS: NonNegativeInt | None = Field(
        default=_MongoDefaults.TIMEOUT_MS,
        description="Operation timeout (ms), None means no timeout",
    )

    # Retry behavior
    RETRY_WRITES: bool = Field(
        default=_MongoDefaults.RETRY_WRITES,
        description="Enable retryable writes",
    )
    RETRY_READS: bool = Field(
        default=_MongoDefaults.RETRY_READS,
        description="Enable retryable reads",
    )

    # TLS/SSL
    TLS: bool = Field(
        default=_MongoDefaults.TLS,
        description="Enable TLS encryption",
    )
    TLS_INSECURE: bool = Field(
        default=_MongoDefaults.TLS_INSECURE,
        description="Specify whether TLS constraints should "
        "be relaxed as much as possible",
    )
    TLS_ALLOW_INVALID_CERTIFICATES: bool = Field(
        default=_MongoDefaults.TLS_ALLOW_INVALID_CERTIFICATES,
        description="Allow invalid TLS certificates",
    )
    TLS_ALLOW_INVALID_HOSTNAMES: bool = Field(
        default=_MongoDefaults.TLS_ALLOW_INVALID_HOSTNAMES,
        description="Allow mismatched TLS certificate hostnames",
    )
    TLS_CA_FILE: str | None = Field(
        default=_MongoDefaults.TLS_CA_FILE,
        description="Path to custom CA file for TLS validation",
        min_length=1,
    )
    TLS_CERTIFICATE_KEY_FILE: str | None = Field(
        default=_MongoDefaults.TLS_CERTIFICATE_KEY_FILE,
        description="Path to client certificate and key file",
        min_length=1,
    )
    TLS_CRL_FILE: str | None = Field(
        default=_MongoDefaults.TLS_CRL_FILE,
        description="Path to file containing a PEM or DER "
        "formatted certificate revocation list",
        min_length=1,
    )
    TLS_CERTIFICATE_KEY_FILE_PASSWORD: str | None = Field(
        default=_MongoDefaults.TLS_CERTIFICATE_KEY_FILE_PASSWORD,
        description="The password or passphrase for "
        "decrypting the private key in ``tlsCertificateKeyFile``. "
        "Only necessary if the private key is encrypted",
        min_length=1,
    )
    TLS_DISABLE_OCSP_ENDPOINT_CHECK: bool = Field(
        default=_MongoDefaults.TLS_DISABLE_OCSP_ENDPOINT_CHECK,
        description="If ``True``, disables certificate revocation status "
        "checking via the OCSP responder specified on "
        "the server certificate",
    )

    # Compression
    COMPRESSORS: str | None = Field(
        default=_MongoDefaults.COMPRESSORS,
        description="Compression method: snappy, zlib, zstd",
        pattern="^(snappy|zlib|zstd)?$",
    )
    ZLIB_COMPRESSION_LEVEL: NonNegativeInt | None = Field(
        default=_MongoDefaults.ZLIB_COMPRESSION_LEVEL,
        description="zlib compression level (0-9)",
        le=9,
    )

    # UUID representation
    UUID_REPRESENTATION: str = Field(
        default=_MongoDefaults.UUID_REPRESENTATION,
        description="UUID representation format",
        pattern="^(standard|pythonLegacy|javaLegacy|csharpLegacy|unspecified)$",
    )

    # Connection mode
    DIRECT_CONNECTION: bool | None = Field(
        default=_MongoDefaults.DIRECT_CONNECTION,
        description="Direct connection to single server",
    )
    APPNAME: str | None = Field(
        default=_MongoDefaults.APPNAME,
        description="Application name (visible in logs)",
        max_length=128,
    )
    READ_PREFERENCE: str | None = Field(
        default=_MongoDefaults.READ_PREFERENCE,
        description="Read preference mode",
        pattern="^(primary|primaryPreferred|secondary|secondaryPreferred|nearest)?$",
    )
    READ_PREFERENCE_TAGS: str | None = Field(
        default=_MongoDefaults.READ_PREFERENCE_TAGS,
        description="Specifies a tag set as a comma-separated list "
        "of colon-separated key-value pairs",
    )
    MAX_STALENESS_SECONDS: NonNegativeInt | None = Field(
        default=_MongoDefaults.MAX_STALENESS_SECONDS,
        description="The maximum estimated length of time a replica set "
        "secondary can fall behind the primary in replication "
        "before it will no longer be selected for operations",
        le=90000,
    )
    REPLICA_SET_NAME: str | None = Field(
        default=_MongoDefaults.REPLICA_SET_NAME,
        description="Replica set name",
        min_length=1,
        max_length=128,
    )

    # Authentication
    AUTH_SOURCE: str = Field(
        default=_MongoDefaults.AUTH_SOURCE,
        description="Database to authenticate against",
        min_length=1,
        max_length=64,
    )
    AUTH_MECHANISM: str = Field(
        default=_MongoDefaults.AUTH_MECHANISM,
        description="Authentication mechanism",
        pattern="^(SCRAM-SHA-1|SCRAM-SHA-256)$",
    )

    # Write concern
    WRITE_CONCERN_W: int | str | None = Field(
        default=_MongoDefaults.WRITE_CONCERN_W,
        description="Write concern: number of replicas or 'majority'",
    )
    JOURNAL: bool = Field(
        default=_MongoDefaults.JOURNAL,
        description="Wait for write to be written to journal",
    )
    FSYNC: bool = Field(
        default=_MongoDefaults.FSYNC,
        description="Force the write operation to fsync to disk",
    )

    # Read concern
    READ_CONCERN_LEVEL: str = Field(
        default=_MongoDefaults.READ_CONCERN_LEVEL,
        description="Read concern level: local, majority, linearizable",
        pattern="^(local|majority|linearizable)?$",
    )

    # SRV & API
    SRV_SERVICE_NAME: str = Field(
        default=_MongoDefaults.SRV_SERVICE_NAME,
        description="Service name for DNS SRV lookups",
        min_length=1,
    )
    SRV_MAX_HOSTS: PositiveInt = Field(
        default=_MongoDefaults.SRV_MAX_HOSTS,
        description="Maximum number of hosts to connect to with SRV",
    )

    # Unicode error handling
    UNICODE_DECODE_ERROR_HANDLER: str = Field(
        default=_MongoDefaults.UNICODE_DECODE_ERROR_HANDLER,
        description="Handler for Unicode decode errors: "
        "strict, ignore, replace",
        pattern="^(strict|ignore|replace|backslashreplace|surrogateescape)$",
    )

    @property
    def dsn(self) -> MongoDsn:
        """Generate MongoDB DSN with pre-built query parameters."""
        return MongoDsn.build(
            host=self.HOST,
            port=self.PORT,
            scheme=self.SCHEMA,
            username=self.USERNAME,
            password=self.PASSWORD.get_secret_value(),
        )

    def get_client_kwargs(self) -> dict[str, Any]:
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
            result["maxpoolsize"] = self.MAX_POOL_SIZE
        if self.MIN_POOL_SIZE:
            result["minpoolsize"] = self.MIN_POOL_SIZE
        if self.MAX_IDLE_TIME_MS:
            result["maxidletimems"] = self.MAX_IDLE_TIME_MS
        if self.MAX_CONNECTING:
            result["maxconnecting"] = self.MAX_CONNECTING
        if self.HEARTBEAT_FREQUENCY_MS:
            result["heartbeatfrequencyms"] = self.HEARTBEAT_FREQUENCY_MS
        if self.SERVER_MONITORING_MODE:
            result["servermonitoringmode"] = self.SERVER_MONITORING_MODE

    def _timeouts_setting(self, result: dict[str, Any]) -> None:
        result["sockettimeoutms"] = self.SOCKET_TIMEOUT_MS
        result["connecttimeoutms"] = self.CONNECT_TIMEOUT_MS
        result["serverselectiontimeoutms"] = self.SERVER_SELECTION_TIMEOUT_MS

        if self.TIMEOUT_MS:
            result["timeoutms"] = self.TIMEOUT_MS
        if self.WAIT_QUEUE_TIMEOUT_MS:
            result["waitqueuetimeoutms"] = self.WAIT_QUEUE_TIMEOUT_MS

    def _retry_behavior(self, result: dict[str, Any]) -> None:
        result["retrywrites"] = self.RETRY_WRITES
        result["retryreads"] = self.RETRY_READS

    def _tls_setting(self, result: dict[str, Any]) -> None:
        if self.TLS:
            result["tls"] = self.TLS
            result["tlsInsecure"] = self.TLS_INSECURE
            result["tlsallowinvalidcertificates"] = (
                self.TLS_ALLOW_INVALID_CERTIFICATES
            )
            result["tlsallowinvalidhostnames"] = (
                self.TLS_ALLOW_INVALID_HOSTNAMES
            )
            result["tlsDisableOCSPEndpointCheck"] = (
                self.TLS_DISABLE_OCSP_ENDPOINT_CHECK
            )

            if self.TLS_CA_FILE:
                result["tlscafile"] = self.TLS_CA_FILE
            if self.TLS_CERTIFICATE_KEY_FILE:
                result["tlscertificatekeyfile"] = self.TLS_CERTIFICATE_KEY_FILE
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
            result["zlibcompressionlevel"] = self.ZLIB_COMPRESSION_LEVEL

    def _uuid_representation_setting(self, result: dict[str, Any]) -> None:
        result["uuidrepresentation"] = self.UUID_REPRESENTATION

    def _connection_mode_setting(self, result: dict[str, Any]) -> None:
        if self.APPNAME:
            result["appname"] = self.APPNAME
        if self.DIRECT_CONNECTION:
            result["directconnection"] = self.DIRECT_CONNECTION
        if self.READ_PREFERENCE:
            result["readpreference"] = self.READ_PREFERENCE
        if self.READ_PREFERENCE_TAGS:
            result["readPreferenceTags"] = self.READ_PREFERENCE_TAGS
        if self.MAX_STALENESS_SECONDS:
            result["maxStalenessSeconds"] = self.MAX_STALENESS_SECONDS
        if self.REPLICA_SET_NAME:
            result["replicaSet"] = self.REPLICA_SET_NAME

    def _authentication_setting(self, result: dict[str, Any]) -> None:
        result["authsource"] = self.AUTH_SOURCE
        result["authmechanism"] = self.AUTH_MECHANISM

    def _write_concern_setting(self, result: dict[str, Any]) -> None:
        result["journal"] = self.JOURNAL
        result["fsync"] = self.FSYNC

        if self.WRITE_CONCERN_W:
            result["w"] = self.WRITE_CONCERN_W

    def _read_concern_setting(self, result: dict[str, Any]) -> None:
        result["readconcernlevel"] = self.READ_CONCERN_LEVEL

    def _srv_api_setting(self, result: dict[str, Any]) -> None:
        result["srvservicename"] = self.SRV_SERVICE_NAME
        result["srvmaxhosts"] = self.SRV_MAX_HOSTS

    def _unicode_error_handling_setting(self, result: dict[str, Any]) -> None:
        result["unicode_decode_error_handler"] = (
            self.UNICODE_DECODE_ERROR_HANDLER
        )
