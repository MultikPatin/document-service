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


@final
class ConnectionDefaults:
    HOST: Final[str] = "localhost"
    PORT: Final[int] = 27017
    USERNAME: Final[str] = ""
    PASSWORD: Final[str] = ""
    SCHEMA: Final[str] = "mongodb"
    DATABASE: Final[str] = "default-database"


@final
class PoolDefaults:
    MAX_SIZE: Final[int] = 100
    MIN_SIZE: Final[int] = 0
    MAX_IDLE_TIME_MS: Final[int] = 0
    MAX_CONNECTING: Final[int] = 5
    WAIT_QUEUE_TIMEOUT_MS: Final[int] = 0
    HEARTBEAT_FREQUENCY_MS: Final[int] = 10000
    SERVER_MONITORING_MODE: Final[str | None] = "auto"


@final
class TimeoutsDefaults:
    CONNECTION_MS: Final[int] = 20000
    SOCKET_MS: Final[int] = 20000
    SERVER_SELECTION_MS: Final[int] = 30000
    OPERATION_MS: Final[int] = 10000


@final
class RetryBehaviorDefaults:
    WRITES: Final[bool] = True
    READS: Final[bool] = True


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
class CompressionDefaults:
    COMPRESSORS: Final[str | None] = None
    ZLIB_COMPRESSION_LEVEL: Final[int | None] = None


@final
class RepresentationDefaults:
    UUID: Final[str] = "standard"


@final
class ConnectionModeDefaults:
    DIRECT_CONNECTION: Final[bool | None] = None
    APPNAME: Final[str | None] = None
    READ_PREFERENCE: Final[str | None] = None
    READ_PREFERENCE_TAGS: Final[str | None] = None
    MAX_STALENESS_SECONDS: Final[int | None] = None
    REPLICA_SET_NAME: Final[str | None] = None


@final
class AuthenticationDefaults:
    SOURCE: Final[str] = "admin"
    MECHANISM: Final[str] = "SCRAM-SHA-256"
    MECHANISM_PROPERTIES: Final[str | None] = None


@final
class WriteConcernDefaults:
    W: Final[int | str | None] = None
    JOURNAL: Final[bool] = False
    FSYNC: Final[bool] = False


@final
class ReadConcernDefaults:
    LEVEL: Final[str] = "majority"


@final
class SRVDefaults:
    SERVICE_NAME: Final[str] = "mongodb"
    MAX_HOSTS: Final[int] = 1


@final
class ErrorHandlingDefaults:
    UNICODE_DECODE: Final[str] = "strict"
