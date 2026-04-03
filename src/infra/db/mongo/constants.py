from typing import Final, final

from pydantic import SecretStr


@final
class _Defaults:
    """
    Class containing default values for MongoDB configuration.

    This class defines all standard parameter values used when connecting
    to MongoDB. All values are declared as Final, making them immutable
    after definition.

    Attributes:
        ENV_PREFIX: Environment variable prefix for MongoDB
        HOST: Default MongoDB host (localhost)
        PORT: Default MongoDB port (27017)
        USERNAME: Default MongoDB username ("")
        PASSWORD: Default MongoDB password ("")
        SCHEMA: Connection scheme (mongodb or mongodb+srv)
        (datetime_ms, datetime, datetime_auto, datetime_clamp)
        DATABASE: Default MongoDB database name (default-db)
        MAX_POOL_SIZE: Maximum number of connections in the pool
        MIN_POOL_SIZE: Minimum number of connections in the pool
        MAX_IDLE_TIME_MS: Maximum idle time for a connection in milliseconds
        MAX_CONNECTING: Maximum number of concurrent connections
        WAIT_QUEUE_TIMEOUT_MS: Timeout for waiting for a free connection
        from the pool
        HEARTBEAT_FREQUENCY_MS: Server monitoring heartbeat frequency
        SERVER_MONITORING_MODE: Server monitoring mode (auto, stream, poll)
        CONNECT_TIMEOUT_MS: Connection establishment timeout
        SOCKET_TIMEOUT_MS: Socket timeout
        SERVER_SELECTION_TIMEOUT_MS: Server selection timeout
        TIMEOUT_MS: Operation timeout
        RETRY_WRITES: Enable retryable write operations on network errors
        RETRY_READS: Enable retryable read operations on network errors
        TLS: Use TLS/SSL encryption
        TLS_INSECURE: Allow invalid certificates and hostname mismatches
        TLS_ALLOW_INVALID_CERTIFICATES: Allow invalid certificates
        TLS_ALLOW_INVALID_HOSTNAMES: Allow hostname mismatches
        TLS_CA_FILE: Path to CA certificates
        TLS_CERTIFICATE_KEY_FILE: Path to client certificate
        TLS_CRL_FILE: Path to Certificate Revocation List
        TLS_CERTIFICATE_KEY_FILE_PASSWORD: Password for the client certificate
        TLS_DISABLE_OCSP_ENDPOINT_CHECK: Disable OCSP endpoint check
        COMPRESSORS: List of compressors (snappy, zlib, zstd)
        ZLIB_COMPRESSION_LEVEL: zlib compression level
        UUID_REPRESENTATION: UUID representation format
        DIRECT_CONNECTION: Direct connection to specified host
        APPNAME: Application name for logs
        READ_PREFERENCE: Read preference (primary, secondary, etc.)
        READ_PREFERENCE_TAGS: Tag set for read preference
        MAX_STALENESS_SECONDS: Maximum replication lag for secondary reads
        REPLICA_SET_NAME: Replica set name
        AUTH_SOURCE: Authentication database
        AUTH_MECHANISM: Authentication mechanism
        WRITE_CONCERN_W: Write concern (number of replicas)
        JOURNAL: Wait for write to be written to journal
        FSYNC: Wait for write to be flushed to disk
        READ_CONCERN_LEVEL: Read concern level
        SRV_SERVICE_NAME: Service name for SRV lookups
        SRV_MAX_HOSTS: Maximum number of hosts when using SRV
        UNICODE_DECODE_ERROR_HANDLER: Unicode decode error handler
    """

    # Connection basics
    ENV_PREFIX: Final[str] = "MONGODB_"
    HOST: Final[str] = "localhost"
    PORT: Final[int] = 27017
    USERNAME: Final[str] = ""
    PASSWORD: Final[SecretStr] = SecretStr("")
    SCHEMA: Final[str] = "mongodb"
    DATABASE: Final[str] = "default-db"
    # Pool settings
    MAX_POOL_SIZE: Final[int | None] = None  # 100
    MIN_POOL_SIZE: Final[int | None] = None  # 0
    MAX_IDLE_TIME_MS: Final[int | None] = None
    MAX_CONNECTING: Final[int | None] = None  # 2
    WAIT_QUEUE_TIMEOUT_MS: Final[int | None] = None
    HEARTBEAT_FREQUENCY_MS: Final[int | None] = None  # 10000
    SERVER_MONITORING_MODE: Final[str | None] = None  # "auto"
    # Timeouts
    CONNECT_TIMEOUT_MS: Final[int] = 20000
    SOCKET_TIMEOUT_MS: Final[int] = 20000
    SERVER_SELECTION_TIMEOUT_MS: Final[int] = 30000
    TIMEOUT_MS: Final[int | None] = 10000
    # Retry behavior
    RETRY_WRITES: Final[bool] = True
    RETRY_READS: Final[bool] = True
    # TLS/SSL
    TLS: Final[bool] = False
    TLS_INSECURE: Final[bool] = False
    TLS_ALLOW_INVALID_CERTIFICATES: Final[bool] = False
    TLS_ALLOW_INVALID_HOSTNAMES: Final[bool] = False
    TLS_CA_FILE: Final[str | None] = None
    TLS_CERTIFICATE_KEY_FILE: Final[str | None] = None
    TLS_CRL_FILE: Final[str | None] = None
    TLS_CERTIFICATE_KEY_FILE_PASSWORD: Final[str | None] = None
    TLS_DISABLE_OCSP_ENDPOINT_CHECK: Final[bool] = False
    # Compression
    COMPRESSORS: Final[str | None] = None
    ZLIB_COMPRESSION_LEVEL: Final[int | None] = None
    # UUID representation
    UUID_REPRESENTATION: Final[str] = "standard"
    # Connection mode
    DIRECT_CONNECTION: Final[bool | None] = None
    APPNAME: Final[str | None] = None
    READ_PREFERENCE: Final[str | None] = None
    READ_PREFERENCE_TAGS: Final[str | None] = None
    MAX_STALENESS_SECONDS: Final[int | None] = None
    REPLICA_SET_NAME: Final[str | None] = None
    # Authentication
    AUTH_SOURCE: Final[str] = "admin"
    AUTH_MECHANISM: Final[str] = "SCRAM-SHA-256"
    # Write concern
    WRITE_CONCERN_W: Final[int | str | None] = None
    JOURNAL: Final[bool] = False
    FSYNC: Final[bool] = False
    # Read concern
    READ_CONCERN_LEVEL: Final[str] = "majority"
    # SRV & API
    SRV_SERVICE_NAME: Final[str] = "mongodb"
    SRV_MAX_HOSTS: Final[int] = 1
    # Unicode error handling
    UNICODE_DECODE_ERROR_HANDLER: Final[str] = "strict"


@final
class _Keys:
    """
    Class containing constants for MongoDB operators and keys.

    This class defines standard MongoDB operators used in queries,
    aggregations, and other operations. All values are declared as Final,
    making them immutable after definition.

    Aggregation and queries:
        id: Document identifier key (_id)
        gte: Greater than or equal operator ($gte)
        gt: Greater than operator ($gt)
        lte: Less than or equal operator ($lte)
        lt: Less than operator ($lt)
        match: Aggregation match operator ($match)
        lookup: Collection join operator ($lookup)
        unwind: Array unwinding operator ($unwind)
        project: Field projection operator ($project)
        set: Value setting operator ($set)
        sort: Sorting operator ($sort)
        skip: Document skipping operator ($skip)
        limit: Document limiting operator ($limit)
        facet: Faceted aggregation operator ($facet)
        count: Document counting operator ($count)

    Array and string operations:
        all: Array element checking operator ($all)
        regex: Regular expression operator ($regex)
        options: Regular expression options ($options)
        in_: Array value presence check operator ($in)
        inc: Value increment operator ($inc)
    """

    id: Final[str] = "_id"
    gte: Final[str] = "$gte"
    gt: Final[str] = "$gt"
    lte: Final[str] = "$lte"
    lt: Final[str] = "$lt"
    match: Final[str] = "$match"
    lookup: Final[str] = "$lookup"
    unwind: Final[str] = "$unwind"
    project: Final[str] = "$project"
    set: Final[str] = "$set"
    sort: Final[str] = "$sort"
    skip: Final[str] = "$skip"
    limit: Final[str] = "$limit"
    facet: Final[str] = "$facet"
    count: Final[str] = "$count"
    all: Final[str] = "$all"
    regex: Final[str] = "$regex"
    options: Final[str] = "$options"
    in_: Final[str] = "$in"
    inc: Final[str] = "$inc"
