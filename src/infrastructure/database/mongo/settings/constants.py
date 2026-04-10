from enum import StrEnum
from typing import Final, Literal, final


@final
class BaseDefaults:
    ENV_FILE: Final[str] = ".env"
    ENV_PREFIX: Final[str] = "MONGODB_"
    ENV_FILE_ENCODING: Final[str] = "utf-8"
    ENV_NESTED_DELIMITER: Final[str] = "__"
    EXTRA: Final[Literal["allow", "ignore", "forbid"]] = "ignore"
    FROZEN: Final[bool] = True
    DB_NAME: Final[str] = "default-db"


# ---- CONNECTION


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


# ---- POOL


class PoolServerMonitoringModEenum(StrEnum):
    auto = "auto"
    stream = "stream"
    poll = "poll"


@final
class PoolDefaults:
    MAX_SIZE: Final[int] = 100
    MIN_SIZE: Final[int] = 0
    MAX_IDLE_TIME_MS: Final[int | None] = None
    MAX_CONNECTING: Final[int | None] = None
    WAIT_QUEUE_TIMEOUT_MS: Final[int | None] = None
    HEARTBEAT_FREQUENCY_MS: Final[int] = 10000
    SERVER_MONITORING_MODE: Final[PoolServerMonitoringModEenum | None] = (
        PoolServerMonitoringModEenum.auto
    )


@final
class PoolKeys:
    MAX_SIZE = "maxPoolSize"
    MIN_SIZE = "minPoolSize"
    MAX_IDLE_TIME = "maxIdleTimeMS"
    MAX_CONNECTING = "maxConnecting"
    WAIT_QUEUE_TIMEOUT = "waitQueueTimeoutMS"
    HEARTBEAT_FREQUENCY = "heartbeatFrequencyMS"
    SERVER_MONITORING_MODE = "serverMonitoringMode"


# ---- TIMEOUTS


@final
class TimeoutsDefaults:
    CONNECTION_MS: Final[int] = 20000
    SOCKET_MS: Final[int] = 20000
    SERVER_SELECTION_MS: Final[int] = 30000
    OPERATION_MS: Final[int] = 10000


@final
class TimeoutsKeys:
    CONNECTION: Final[str] = "connectTimeoutMS"
    SOCKET: Final[str] = "socketTimeoutMS"
    SERVER_SELECTION: Final[str] = "serverSelectionTimeoutMS"
    OPERATION: Final[str] = "timeoutMS"


# ---- RETRY BEHAVIOR


@final
class RetryBehaviorDefaults:
    WRITES: Final[bool] = True
    READS: Final[bool] = True


@final
class RetryBehaviorKeys:
    WRITES: Final[str] = "retryWrites"
    READS: Final[str] = "retryReads"


# ---- TLS


@final
class TLSDefaults:
    ENABLE: Final[bool] = False
    INSECURE: Final[bool] = False
    ALLOW_INVALID_CERTIFICATES: Final[bool] = False
    ALLOW_INVALID_HOSTNAMES: Final[bool] = False
    CA_FILE: Final[str | None] = None
    CERTIFICATE_KEY_FILE: Final[str | None] = None
    CRL_FILE: Final[str | None] = None
    CERTIFICATE_KEY_FILE_PASSWORD: Final[str | None] = None
    DISABLE_OCSP_ENDPOINT_CHECK: Final[bool] = False


@final
class TLSKeys:
    ENABLE: Final[str] = "tls"
    INSECURE: Final[str] = "tlsInsecure"
    ALLOW_INVALID_CERTIFICATES: Final[str] = "tlsAllowInvalidCertificates"
    ALLOW_INVALID_HOSTNAMES: Final[str] = "tlsAllowInvalidHostnames"
    CA_FILE: Final[str] = "tlsCAFile"
    CERTIFICATE_KEY_FILE: Final[str] = "tlsCertificateKeyFile"
    CRL_FILE: Final[str] = "tlsCRLFile"
    CERTIFICATE_KEY_FILE_PASSWORD: Final[str] = "tlsCertificateKeyFilePassword"  # noqa: S105
    DISABLE_OCSP_ENDPOINT_CHECK: Final[str] = "tlsDisableOCSPEndpointCheck"


# ---- COMPRESSION


class CompressorsEnum(StrEnum):
    SNAPPY = "snappy"
    ZLIB = "zlib"
    ZSTD = "zstd"


@final
class CompressionDefaults:
    COMPRESSORS: Final[CompressorsEnum | None] = None
    ZLIB_COMPRESSION_LEVEL: Final[int | None] = None


@final
class CompressionKeys:
    COMPRESSORS = "compressors"
    ZLIB_COMPRESSION_LEVEL = "zlibCompressionLevel"


# ---- REPRESENTATION


class RepresentationUuidEnum(StrEnum):
    standard = "standard"
    python_legacy = "pythonLegacy"
    java_legacy = "javaLegacy"
    csharp_legacy = "csharpLegacy"
    unspecified = "unspecified"


@final
class RepresentationDefaults:
    UUID: Final[RepresentationUuidEnum] = RepresentationUuidEnum.standard


@final
class RepresentationKeys:
    UUID: Final[str] = "uuidRepresentation"


# ---- CONNECTION MODE


class ConnectionModeReadPreferenceEnum(StrEnum):
    primary = "primary"
    secondary = "secondary"
    primary_preferred = "primaryPreferred"
    secondary_preferred = "secondaryPreferred"
    nearest = "nearest"


@final
class ConnectionModeDefaults:
    DIRECT_CONNECTION: Final[bool | None] = None
    APPNAME: Final[str | None] = None
    READ_PREFERENCE: Final[ConnectionModeReadPreferenceEnum | None] = None
    READ_PREFERENCE_TAGS: Final[str | None] = None
    MAX_STALENESS_SECONDS: Final[int | None] = None
    REPLICA_SET_NAME: Final[str | None] = None


@final
class ConnectionModeKeys:
    DIRECT_CONNECTION = "directConnection"
    APPNAME = "appname"
    READ_PREFERENCE = "readPreference"
    READ_PREFERENCE_TAGS = "readPreferenceTags"
    MAX_STALENESS_SECONDS = "maxStalenessSeconds"
    REPLICA_SET_NAME = "replicaSet"


# ---- AUTHENTICATION


class AuthenticationMechanismEnum(StrEnum):
    SCRAM_SHA_1 = "SCRAM-SHA-1"
    SCRAM_SHA_256 = "SCRAM-SHA-256"


@final
class AuthenticationDefaults:
    SOURCE: Final[str] = "admin"
    MECHANISM: Final[AuthenticationMechanismEnum] = (
        AuthenticationMechanismEnum.SCRAM_SHA_256
    )
    MECHANISM_PROPERTIES: Final[str | None] = None


@final
class AuthenticationKeys:
    SOURCE: Final[str] = "authSource"
    MECHANISM: Final[str] = "authMechanism"
    MECHANISM_PROPERTIES: Final[str] = "authMechanismProperties"


# ---- WRITE CONCERN


@final
class WriteConcernDefaults:
    W: Final[int | str | None] = None
    JOURNAL: Final[bool] = False
    FSYNC: Final[bool] = False


@final
class WriteConcernKeys:
    W: Final[str] = "w"
    JOURNAL: Final[str] = "journal"
    FSYNC: Final[str] = "fsync"


# ---- READ CONCERN


class ReadConcernLevelEnum(StrEnum):
    local = "local"
    majority = "majority"
    linearizable = "linearizable"


@final
class ReadConcernDefaults:
    LEVEL: Final[ReadConcernLevelEnum] = ReadConcernLevelEnum.majority


@final
class ReadConcernKeys:
    LEVEL: Final[str] = "readConcernLevel"


# ---- SRV API


@final
class SRVDefaults:
    SERVICE_NAME: Final[str] = "mongodb"
    MAX_HOSTS: Final[int] = 1


@final
class SRVKeys:
    SERVICE_NAME: Final[str] = "srvServiceName"
    MAX_HOSTS: Final[str] = "srvMaxHosts"


# ---- ERROR HANDLING


class ErrorHandlingUnicodeDecodeEnum(StrEnum):
    strict = "strict"
    ignore = "ignore"
    replace = "replace"
    backslashreplace = "backslashreplace"
    surrogate_escape = "surrogateescape"


@final
class ErrorHandlingDefaults:
    UNICODE_DECODE: Final[ErrorHandlingUnicodeDecodeEnum] = (
        ErrorHandlingUnicodeDecodeEnum.strict
    )


@final
class ErrorHandlingKeys:
    UNICODE_DECODE = "unicode_decode_error_handler"
