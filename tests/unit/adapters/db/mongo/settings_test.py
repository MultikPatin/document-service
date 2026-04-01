import pytest
from pydantic import SecretStr, ValidationError

from src.adapters.db.mongo.constants import _MongoDefaults
from src.adapters.db.mongo.settings import _Settings
from src.core.settings.constants import Defaults


def test_settings_default_initialization():
    """Test that all fields are initialized with correct default values from constants."""
    settings = _Settings()

    # Connection basics
    assert settings.HOST == Defaults.HOST
    assert settings.PORT == _MongoDefaults.PORT
    assert settings.USERNAME == Defaults.USERNAME
    assert (
        settings.PASSWORD.get_secret_value()
        == Defaults.PASSWORD.get_secret_value()
    )
    assert settings.SCHEMA == _MongoDefaults.SCHEMA
    assert settings.DATABASE == Defaults.DATABASE

    # Pool settings
    assert settings.MAX_POOL_SIZE == _MongoDefaults.MAX_POOL_SIZE
    assert settings.MIN_POOL_SIZE == _MongoDefaults.MIN_POOL_SIZE
    assert settings.MAX_IDLE_TIME_MS == _MongoDefaults.MAX_IDLE_TIME_MS
    assert settings.MAX_CONNECTING == _MongoDefaults.MAX_CONNECTING
    assert (
        settings.WAIT_QUEUE_TIMEOUT_MS == _MongoDefaults.WAIT_QUEUE_TIMEOUT_MS
    )
    assert (
        settings.HEARTBEAT_FREQUENCY_MS == _MongoDefaults.HEARTBEAT_FREQUENCY_MS
    )
    assert (
        settings.SERVER_MONITORING_MODE == _MongoDefaults.SERVER_MONITORING_MODE
    )

    # Timeouts
    assert settings.CONNECT_TIMEOUT_MS == _MongoDefaults.CONNECT_TIMEOUT_MS
    assert settings.SOCKET_TIMEOUT_MS == _MongoDefaults.SOCKET_TIMEOUT_MS
    assert (
        settings.SERVER_SELECTION_TIMEOUT_MS
        == _MongoDefaults.SERVER_SELECTION_TIMEOUT_MS
    )
    assert settings.TIMEOUT_MS == _MongoDefaults.TIMEOUT_MS

    # Retry behavior
    assert settings.RETRY_WRITES is _MongoDefaults.RETRY_WRITES
    assert settings.RETRY_READS is _MongoDefaults.RETRY_READS

    # TLS/SSL
    assert settings.TLS is _MongoDefaults.TLS
    assert settings.TLS_INSECURE is _MongoDefaults.TLS_INSECURE
    assert (
        settings.TLS_ALLOW_INVALID_CERTIFICATES
        is _MongoDefaults.TLS_ALLOW_INVALID_CERTIFICATES
    )
    assert (
        settings.TLS_ALLOW_INVALID_HOSTNAMES
        is _MongoDefaults.TLS_ALLOW_INVALID_HOSTNAMES
    )
    assert settings.TLS_CA_FILE == _MongoDefaults.TLS_CA_FILE
    assert (
        settings.TLS_CERTIFICATE_KEY_FILE
        == _MongoDefaults.TLS_CERTIFICATE_KEY_FILE
    )
    assert settings.TLS_CRL_FILE == _MongoDefaults.TLS_CRL_FILE
    assert (
        settings.TLS_CERTIFICATE_KEY_FILE_PASSWORD
        == _MongoDefaults.TLS_CERTIFICATE_KEY_FILE_PASSWORD
    )
    assert (
        settings.TLS_DISABLE_OCSP_ENDPOINT_CHECK
        is _MongoDefaults.TLS_DISABLE_OCSP_ENDPOINT_CHECK
    )

    # Compression
    assert settings.COMPRESSORS == _MongoDefaults.COMPRESSORS
    assert (
        settings.ZLIB_COMPRESSION_LEVEL == _MongoDefaults.ZLIB_COMPRESSION_LEVEL
    )

    # UUID representation
    assert settings.UUID_REPRESENTATION == _MongoDefaults.UUID_REPRESENTATION

    # Connection mode
    assert settings.DIRECT_CONNECTION is _MongoDefaults.DIRECT_CONNECTION
    assert settings.APPNAME == _MongoDefaults.APPNAME
    assert settings.READ_PREFERENCE == _MongoDefaults.READ_PREFERENCE
    assert settings.READ_PREFERENCE_TAGS == _MongoDefaults.READ_PREFERENCE_TAGS
    assert (
        settings.MAX_STALENESS_SECONDS == _MongoDefaults.MAX_STALENESS_SECONDS
    )
    assert settings.REPLICA_SET_NAME == _MongoDefaults.REPLICA_SET_NAME

    # Authentication
    assert settings.AUTH_SOURCE == _MongoDefaults.AUTH_SOURCE
    assert settings.AUTH_MECHANISM == _MongoDefaults.AUTH_MECHANISM

    # Write concern
    assert settings.WRITE_CONCERN_W == _MongoDefaults.WRITE_CONCERN_W
    assert settings.JOURNAL is _MongoDefaults.JOURNAL
    assert settings.FSYNC is _MongoDefaults.FSYNC

    # Read concern
    assert settings.READ_CONCERN_LEVEL == _MongoDefaults.READ_CONCERN_LEVEL

    # SRV & API
    assert settings.SRV_SERVICE_NAME == _MongoDefaults.SRV_SERVICE_NAME
    assert settings.SRV_MAX_HOSTS == _MongoDefaults.SRV_MAX_HOSTS

    # Unicode error handling
    assert (
        settings.UNICODE_DECODE_ERROR_HANDLER
        == _MongoDefaults.UNICODE_DECODE_ERROR_HANDLER
    )


def test_dsn_generation():
    """Test DSN generation with various combinations using constants."""
    # Basic DSN
    settings = _Settings()
    expected_dsn = f"{settings.SCHEMA}://{settings.HOST}:{settings.PORT}"
    assert str(settings.dsn) == expected_dsn

    # With username and password
    username = "user1"
    password = "pass123"
    settings = _Settings(USERNAME=username, PASSWORD=SecretStr(password))
    expected_dsn = f"{settings.SCHEMA}://{username}:{password}@{settings.HOST}:{settings.PORT}"
    assert str(settings.dsn) == expected_dsn

    # With different schema (SRV)
    schema = "mongodb+srv"
    host = "cluster0.example.com"
    settings = _Settings(
        SCHEMA=schema,
        HOST=host,
    )
    expected_dsn = f"{schema}://{host}:{settings.PORT}"
    assert str(settings.dsn) == expected_dsn

    # With port
    settings = _Settings(PORT=27018)
    expected_dsn = f"{settings.SCHEMA}://{settings.HOST}:{settings.PORT}"
    # Fix for double slash when database is empty
    assert str(settings.dsn) == expected_dsn


def test_get_client_kwargs_pool_settings():
    """Test pool settings in get_client_kwargs."""
    # All pool settings provided
    max_pool_size = 50
    min_pool_size = 5
    max_idle_time_ms = 20000
    max_connecting = 50
    wait_queue_timeout_ms = 5000
    heartbeat_frequency_ms = 500
    server_monitoring_mode = "poll"

    settings = _Settings(
        MAX_POOL_SIZE=max_pool_size,
        MIN_POOL_SIZE=min_pool_size,
        MAX_IDLE_TIME_MS=max_idle_time_ms,
        MAX_CONNECTING=max_connecting,
        WAIT_QUEUE_TIMEOUT_MS=wait_queue_timeout_ms,
        HEARTBEAT_FREQUENCY_MS=heartbeat_frequency_ms,
        SERVER_MONITORING_MODE=server_monitoring_mode,
    )
    kwargs = settings.get_client_kwargs()
    assert kwargs["maxpoolsize"] == max_pool_size
    assert kwargs["minpoolsize"] == min_pool_size
    assert kwargs["maxidletimems"] == max_idle_time_ms
    assert kwargs["maxconnecting"] == max_connecting
    assert kwargs["waitqueuetimeoutms"] == wait_queue_timeout_ms
    assert kwargs["heartbeatfrequencyms"] == heartbeat_frequency_ms
    assert kwargs["servermonitoringmode"] == server_monitoring_mode

    # None values should be excluded
    settings = _Settings(
        MAX_POOL_SIZE=None,
        MIN_POOL_SIZE=None,
        MAX_IDLE_TIME_MS=None,
        MAX_CONNECTING=None,
        WAIT_QUEUE_TIMEOUT_MS=None,
        HEARTBEAT_FREQUENCY_MS=None,
        SERVER_MONITORING_MODE=None,
    )
    kwargs = settings.get_client_kwargs()
    assert "maxpoolsize" not in kwargs
    assert "minpoolsize" not in kwargs
    assert "maxidletimems" not in kwargs
    assert "maxconnecting" not in kwargs
    assert "waitqueuetimeoutms" not in kwargs
    assert "heartbeatfrequencyms" not in kwargs
    assert "servermonitoringmode" not in kwargs


def test_get_client_kwargs_timeouts():
    """Test timeout settings in get_client_kwargs."""
    connect_timeout_ms = 5000
    socket_timeout_ms = 15000
    server_selection_timeout_ms = 45000
    timeout_ms = 60000
    wait_queue_timeout_ms = 20000

    settings = _Settings(
        CONNECT_TIMEOUT_MS=connect_timeout_ms,
        SOCKET_TIMEOUT_MS=socket_timeout_ms,
        SERVER_SELECTION_TIMEOUT_MS=server_selection_timeout_ms,
        TIMEOUT_MS=timeout_ms,
        WAIT_QUEUE_TIMEOUT_MS=wait_queue_timeout_ms,
    )
    kwargs = settings.get_client_kwargs()
    assert kwargs["connecttimeoutms"] == connect_timeout_ms
    assert kwargs["sockettimeoutms"] == socket_timeout_ms
    assert kwargs["serverselectiontimeoutms"] == server_selection_timeout_ms
    assert kwargs["timeoutms"] == timeout_ms
    assert kwargs["waitqueuetimeoutms"] == wait_queue_timeout_ms

    # TIMEOUT_MS=None should exclude timeoutms
    settings = _Settings(TIMEOUT_MS=None)
    kwargs = settings.get_client_kwargs()
    assert "timeoutms" not in kwargs


def test_get_client_kwargs_retry_behavior():
    """Test retry behavior settings in get_client_kwargs."""
    retry_writes = False
    retry_reads = False

    settings = _Settings(RETRY_WRITES=retry_writes, RETRY_READS=retry_reads)
    kwargs = settings.get_client_kwargs()
    assert kwargs["retrywrites"] is retry_writes
    assert kwargs["retryreads"] is retry_reads

    retry_writes = True
    retry_reads = True

    settings = _Settings(RETRY_WRITES=retry_writes, RETRY_READS=retry_reads)
    kwargs = settings.get_client_kwargs()
    assert kwargs["retrywrites"] is retry_writes
    assert kwargs["retryreads"] is retry_reads


def test_get_client_kwargs_tls():
    """Test TLS settings in get_client_kwargs."""
    # TLS disabled
    settings = _Settings(TLS=False)
    kwargs = settings.get_client_kwargs()
    assert "tls" not in kwargs
    assert "tlsInsecure" not in kwargs
    assert "tlsallowinvalidcertificates" not in kwargs
    assert "tlsallowinvalidhostnames" not in kwargs
    assert "tlsDisableOCSPEndpointCheck" not in kwargs
    assert "tlscafile" not in kwargs
    assert "tlscertificatekeyfile" not in kwargs
    assert "tlsCRLFile" not in kwargs
    assert "tlsCertificateKeyFilePassword" not in kwargs

    # TLS enabled with all options
    tls = True
    tls_insecure = False
    tls_allow_invalid_certificates = False
    tls_allow_invalid_hostnames = False
    tls_ca_file = "/ca.pem"
    tls_certificate_key_file = "/client.pem"
    tls_crl_file = "/crl.pem"
    tls_certificate_key_file_password = "pass"
    tls_disable_ocsp_endpoint_check = False

    settings = _Settings(
        TLS=tls,
        TLS_INSECURE=tls_insecure,
        TLS_ALLOW_INVALID_CERTIFICATES=tls_allow_invalid_certificates,
        TLS_ALLOW_INVALID_HOSTNAMES=tls_allow_invalid_hostnames,
        TLS_CA_FILE=tls_ca_file,
        TLS_CERTIFICATE_KEY_FILE=tls_certificate_key_file,
        TLS_CRL_FILE=tls_crl_file,
        TLS_CERTIFICATE_KEY_FILE_PASSWORD=tls_certificate_key_file_password,
        TLS_DISABLE_OCSP_ENDPOINT_CHECK=tls_disable_ocsp_endpoint_check,
    )
    kwargs = settings.get_client_kwargs()
    assert kwargs["tls"] is tls
    assert kwargs["tlsInsecure"] is tls_insecure
    assert (
        kwargs["tlsallowinvalidcertificates"] is tls_allow_invalid_certificates
    )
    assert kwargs["tlsallowinvalidhostnames"] is tls_allow_invalid_hostnames
    assert (
        kwargs["tlsDisableOCSPEndpointCheck"] is tls_disable_ocsp_endpoint_check
    )
    assert kwargs["tlscafile"] == tls_ca_file
    assert kwargs["tlscertificatekeyfile"] == tls_certificate_key_file
    assert kwargs["tlsCRLFile"] == tls_crl_file
    assert (
        kwargs["tlsCertificateKeyFilePassword"]
        == tls_certificate_key_file_password
    )


def test_get_client_kwargs_compression():
    """Test compression settings in get_client_kwargs."""
    # No compression
    settings = _Settings(COMPRESSORS=None, ZLIB_COMPRESSION_LEVEL=None)
    kwargs = settings.get_client_kwargs()
    assert "compressors" not in kwargs
    assert "zlibcompressionlevel" not in kwargs

    # With compression
    compressors = "zlib"
    zlib_compression_level = 6

    settings = _Settings(
        COMPRESSORS=compressors, ZLIB_COMPRESSION_LEVEL=zlib_compression_level
    )
    kwargs = settings.get_client_kwargs()
    assert kwargs["compressors"] == compressors
    assert kwargs["zlibcompressionlevel"] == zlib_compression_level


def test_get_client_kwargs_uuid_representation():
    """Test UUID representation setting in get_client_kwargs."""
    settings = _Settings(UUID_REPRESENTATION="pythonLegacy")
    kwargs = settings.get_client_kwargs()
    assert kwargs["uuidrepresentation"] == "pythonLegacy"


def test_get_client_kwargs_connection_mode():
    """Test connection mode settings in get_client_kwargs."""
    appname = "myapp"
    direct_connection = True
    read_preference = "secondaryPreferred"
    read_preference_tags = "dc:east,type:hot"
    max_staleness_seconds = 120
    replica_set_name = "rs0"

    settings = _Settings(
        APPNAME=appname,
        DIRECT_CONNECTION=direct_connection,
        READ_PREFERENCE=read_preference,
        READ_PREFERENCE_TAGS=read_preference_tags,
        MAX_STALENESS_SECONDS=max_staleness_seconds,
        REPLICA_SET_NAME=replica_set_name,
    )
    kwargs = settings.get_client_kwargs()
    assert kwargs["appname"] == appname
    assert kwargs["directconnection"] is direct_connection
    assert kwargs["readpreference"] == read_preference
    assert kwargs["readPreferenceTags"] == read_preference_tags
    assert kwargs["maxStalenessSeconds"] == max_staleness_seconds
    assert kwargs["replicaSet"] == replica_set_name

    # None values should be excluded
    settings = _Settings(
        APPNAME=None,
        DIRECT_CONNECTION=None,
        READ_PREFERENCE=None,
        READ_PREFERENCE_TAGS=None,
        MAX_STALENESS_SECONDS=None,
        REPLICA_SET_NAME=None,
    )
    kwargs = settings.get_client_kwargs()
    assert "appname" not in kwargs
    assert "directconnection" not in kwargs
    assert "readpreference" not in kwargs
    assert "readPreferenceTags" not in kwargs
    assert "maxStalenessSeconds" not in kwargs
    assert "replicaSet" not in kwargs


def test_get_client_kwargs_authentication():
    """Test authentication settings in get_client_kwargs."""
    auth_source = "mydb"
    auth_mechanism = "SCRAM-SHA-1"

    settings = _Settings(AUTH_SOURCE=auth_source, AUTH_MECHANISM=auth_mechanism)
    kwargs = settings.get_client_kwargs()
    assert kwargs["authsource"] == auth_source
    assert kwargs["authmechanism"] == auth_mechanism


def test_get_client_kwargs_write_concern():
    """Test write concern settings in get_client_kwargs."""
    write_concern_w = 2
    journal = True
    fsync = False

    # With w
    settings = _Settings(
        WRITE_CONCERN_W=write_concern_w, JOURNAL=journal, FSYNC=fsync
    )
    kwargs = settings.get_client_kwargs()
    assert kwargs["w"] == write_concern_w
    assert kwargs["journal"] is journal
    assert kwargs["fsync"] is fsync

    # Without w
    settings = _Settings(WRITE_CONCERN_W=None, JOURNAL=journal, FSYNC=fsync)
    kwargs = settings.get_client_kwargs()
    assert "w" not in kwargs
    assert kwargs["journal"] is journal
    assert kwargs["fsync"] is fsync


def test_get_client_kwargs_read_concern():
    """Test read concern settings in get_client_kwargs."""
    read_concern_level = "majority"

    settings = _Settings(READ_CONCERN_LEVEL=read_concern_level)
    kwargs = settings.get_client_kwargs()
    assert kwargs["readconcernlevel"] == read_concern_level

    read_concern_level = "local"

    settings = _Settings(READ_CONCERN_LEVEL=read_concern_level)
    kwargs = settings.get_client_kwargs()
    assert kwargs["readconcernlevel"] == read_concern_level


def test_get_client_kwargs_srv_api():
    """Test SRV API settings in get_client_kwargs."""
    srv_service_name = "custom"
    srv_max_hosts = 50

    settings = _Settings(
        SRV_SERVICE_NAME=srv_service_name, SRV_MAX_HOSTS=srv_max_hosts
    )
    kwargs = settings.get_client_kwargs()
    assert kwargs["srvservicename"] == srv_service_name
    assert kwargs["srvmaxhosts"] == srv_max_hosts


def test_get_client_kwargs_unicode_error_handling():
    """Test Unicode error handling setting in get_client_kwargs."""
    settings = _Settings(UNICODE_DECODE_ERROR_HANDLER="ignore")
    kwargs = settings.get_client_kwargs()
    assert kwargs["unicode_decode_error_handler"] == "ignore"


def test_get_client_kwargs_full_configuration():  # noqa: PLR0915
    """Test get_client_kwargs with all settings configured."""
    # Pool settings
    max_pool_size = 200
    min_pool_size = 10
    max_idle_time_ms = 30000
    max_connecting = 20
    wait_queue_timeout_ms = 15000
    heartbeat_frequency_ms = 20000
    server_monitoring_mode = "stream"
    # Timeouts
    connect_timeout_ms = 8000
    socket_timeout_ms = 12000
    server_selection_timeout_ms = 35000
    timeout_ms = 45000
    # Retry behavior
    retry_writes = False
    retry_reads = False
    # TLS/SSL
    tls = True
    tls_insecure = False
    tls_allow_invalid_certificates = False
    tls_allow_invalid_hostnames = False
    tls_ca_file = "/ca.pem"
    tls_certificate_key_file = "/client.pem"
    tls_crl_file = "/crl.pem"
    tls_certificate_key_file_password = "pass"
    tls_disable_ocsp_endpoint_check = False
    # Compression
    compressors = "zstd"
    zlib_compression_level = 9
    # UUID representation
    uuid_representation = "standard"
    # Connection mode
    appname = "production-app"
    direct_connection = True
    read_preference = "primary"
    read_preference_tags = "dc:west,type:cold"
    max_staleness_seconds = 60
    replica_set_name = "rs1"
    # Authentication
    auth_source = "admin"
    auth_mechanism = "SCRAM-SHA-256"
    # Write concern
    write_concern_w = "majority"
    journal = True
    fsync = False
    # Read concern
    read_concern_level = "linearizable"
    # SRV & API
    srv_service_name = "mongodb"
    srv_max_hosts = 100
    # Unicode error handling
    unicode_decode_error_handler = "replace"

    settings = _Settings(
        # Pool settings
        MAX_POOL_SIZE=max_pool_size,
        MIN_POOL_SIZE=min_pool_size,
        MAX_IDLE_TIME_MS=max_idle_time_ms,
        MAX_CONNECTING=max_connecting,
        WAIT_QUEUE_TIMEOUT_MS=wait_queue_timeout_ms,
        HEARTBEAT_FREQUENCY_MS=heartbeat_frequency_ms,
        SERVER_MONITORING_MODE=server_monitoring_mode,
        # Timeouts
        CONNECT_TIMEOUT_MS=connect_timeout_ms,
        SOCKET_TIMEOUT_MS=socket_timeout_ms,
        SERVER_SELECTION_TIMEOUT_MS=server_selection_timeout_ms,
        TIMEOUT_MS=timeout_ms,
        # Retry behavior
        RETRY_WRITES=retry_writes,
        RETRY_READS=retry_reads,
        # TLS/SSL
        TLS=tls,
        TLS_INSECURE=tls_insecure,
        TLS_ALLOW_INVALID_CERTIFICATES=tls_allow_invalid_certificates,
        TLS_ALLOW_INVALID_HOSTNAMES=tls_allow_invalid_hostnames,
        TLS_CA_FILE=tls_ca_file,
        TLS_CERTIFICATE_KEY_FILE=tls_certificate_key_file,
        TLS_CRL_FILE=tls_crl_file,
        TLS_CERTIFICATE_KEY_FILE_PASSWORD=tls_certificate_key_file_password,
        TLS_DISABLE_OCSP_ENDPOINT_CHECK=tls_disable_ocsp_endpoint_check,
        # Compression
        COMPRESSORS=compressors,
        ZLIB_COMPRESSION_LEVEL=zlib_compression_level,
        # UUID representation
        UUID_REPRESENTATION=uuid_representation,
        # Connection mode
        APPNAME=appname,
        DIRECT_CONNECTION=direct_connection,
        READ_PREFERENCE=read_preference,
        READ_PREFERENCE_TAGS=read_preference_tags,
        MAX_STALENESS_SECONDS=max_staleness_seconds,
        REPLICA_SET_NAME=replica_set_name,
        # Authentication
        AUTH_SOURCE=auth_source,
        AUTH_MECHANISM=auth_mechanism,
        # Write concern
        WRITE_CONCERN_W=write_concern_w,
        JOURNAL=journal,
        FSYNC=fsync,
        # Read concern
        READ_CONCERN_LEVEL=read_concern_level,
        # SRV & API
        SRV_SERVICE_NAME=srv_service_name,
        SRV_MAX_HOSTS=srv_max_hosts,
        # Unicode error handling
        UNICODE_DECODE_ERROR_HANDLER=unicode_decode_error_handler,
    )

    kwargs = settings.get_client_kwargs()

    # Verify all expected keys are present with correct values
    # Pool settings
    assert kwargs["maxpoolsize"] == max_pool_size
    assert kwargs["minpoolsize"] == min_pool_size
    assert kwargs["maxidletimems"] == max_idle_time_ms
    assert kwargs["maxconnecting"] == max_connecting
    assert kwargs["waitqueuetimeoutms"] == wait_queue_timeout_ms
    assert kwargs["heartbeatfrequencyms"] == heartbeat_frequency_ms
    assert kwargs["servermonitoringmode"] == server_monitoring_mode
    # Timeouts
    assert kwargs["connecttimeoutms"] == connect_timeout_ms
    assert kwargs["sockettimeoutms"] == socket_timeout_ms
    assert kwargs["serverselectiontimeoutms"] == server_selection_timeout_ms
    assert kwargs["timeoutms"] == timeout_ms
    # Retry behavior
    assert kwargs["retrywrites"] is retry_writes
    assert kwargs["retryreads"] is retry_reads
    # TLS/SSL
    assert kwargs["tls"] is tls
    assert kwargs["tlsInsecure"] is tls_insecure
    assert (
        kwargs["tlsallowinvalidcertificates"] is tls_allow_invalid_certificates
    )
    assert kwargs["tlsallowinvalidhostnames"] is tls_allow_invalid_hostnames
    assert kwargs["tlscafile"] == tls_ca_file
    assert kwargs["tlscertificatekeyfile"] == tls_certificate_key_file
    assert kwargs["tlsCRLFile"] == tls_crl_file
    assert (
        kwargs["tlsCertificateKeyFilePassword"]
        == tls_certificate_key_file_password
    )
    assert (
        kwargs["tlsDisableOCSPEndpointCheck"] is tls_disable_ocsp_endpoint_check
    )
    # Compression
    assert kwargs["compressors"] == compressors
    assert kwargs["zlibcompressionlevel"] == zlib_compression_level
    # UUID representation
    assert kwargs["uuidrepresentation"] == uuid_representation
    # Connection mode
    assert kwargs["appname"] == appname
    assert kwargs["directconnection"] is direct_connection
    assert kwargs["readpreference"] == read_preference
    assert kwargs["readPreferenceTags"] == read_preference_tags
    assert kwargs["maxStalenessSeconds"] == max_staleness_seconds
    assert kwargs["replicaSet"] == replica_set_name
    # Authentication
    assert kwargs["authsource"] == auth_source
    assert kwargs["authmechanism"] == auth_mechanism
    # Write concern
    assert kwargs["w"] == write_concern_w
    assert kwargs["journal"] is journal
    assert kwargs["fsync"] is fsync
    # Read concern
    assert kwargs["readconcernlevel"] == read_concern_level
    # SRV & API
    assert kwargs["srvservicename"] == srv_service_name
    assert kwargs["srvmaxhosts"] == srv_max_hosts
    # Unicode error handling
    assert (
        kwargs["unicode_decode_error_handler"] == unicode_decode_error_handler
    )


def test_field_validation_port():
    """Test PORT validation (must be < 65536)."""
    with pytest.raises(ValidationError):
        _Settings(PORT=65536)

    with pytest.raises(ValidationError):
        _Settings(PORT=0)

    # Valid ports
    min_port = 1
    max_port = 65535

    settings = _Settings(PORT=min_port)
    assert min_port == settings.PORT
    settings = _Settings(PORT=max_port)
    assert max_port == settings.PORT


def test_field_validation_username():
    """Test USERNAME validation (max_length=255)."""
    with pytest.raises(ValidationError):
        _Settings(USERNAME="x" * 256)

    # Valid username
    settings = _Settings(USERNAME="x" * 255)
    assert settings.USERNAME == "x" * 255


def test_field_validation_database():
    """Test DATABASE validation (max_length=32)."""
    with pytest.raises(ValidationError):
        _Settings(DATABASE="x" * 33)

    # Valid database
    settings = _Settings(DATABASE="x" * 32)
    assert settings.DATABASE == "x" * 32


def test_field_validation_schema():
    """Test SCHEMA validation (must be mongodb or mongodb+srv)."""
    with pytest.raises(ValidationError):
        _Settings(SCHEMA="invalid")

    # Valid schemas
    settings = _Settings(SCHEMA="mongodb")
    assert settings.SCHEMA == "mongodb"
    settings = _Settings(SCHEMA="mongodb+srv")
    assert settings.SCHEMA == "mongodb+srv"


def test_field_validation_server_monitoring_mode():
    """Test SERVER_MONITORING_MODE validation."""
    with pytest.raises(ValidationError):
        _Settings(SERVER_MONITORING_MODE="invalid")

    # Valid modes
    for mode in ["auto", "stream", "poll"]:
        settings = _Settings(SERVER_MONITORING_MODE=mode)
        assert mode == settings.SERVER_MONITORING_MODE


def test_field_validation_compression():
    """Test COMPRESSORS validation."""
    with pytest.raises(ValidationError):
        _Settings(COMPRESSORS="invalid")

    # Valid compressors
    for comp in ["snappy", "zlib", "zstd", None]:
        settings = _Settings(COMPRESSORS=comp)
        assert comp == settings.COMPRESSORS


def test_field_validation_uuid_representation():
    """Test UUID_REPRESENTATION validation."""
    with pytest.raises(ValidationError):
        _Settings(UUID_REPRESENTATION="invalid")

    # Valid representations
    valid_representations = [
        "standard",
        "pythonLegacy",
        "javaLegacy",
        "csharpLegacy",
        "unspecified",
    ]
    for rep in valid_representations:
        settings = _Settings(UUID_REPRESENTATION=rep)
        assert rep == settings.UUID_REPRESENTATION


def test_field_validation_read_preference():
    """Test READ_PREFERENCE validation."""
    with pytest.raises(ValidationError):
        _Settings(READ_PREFERENCE="invalid")

    # Valid preferences
    valid_preferences = [
        "primary",
        "primaryPreferred",
        "secondary",
        "secondaryPreferred",
        "nearest",
        None,
    ]
    for pref in valid_preferences:
        settings = _Settings(READ_PREFERENCE=pref)
        assert pref == settings.READ_PREFERENCE


def test_field_validation_read_concern_level():
    """Test READ_CONCERN_LEVEL validation."""
    with pytest.raises(ValidationError):
        _Settings(READ_CONCERN_LEVEL="invalid")

    # Valid levels
    valid_levels = ["local", "majority", "linearizable"]
    for level in valid_levels:
        settings = _Settings(READ_CONCERN_LEVEL=level)
        assert level == settings.READ_CONCERN_LEVEL


def test_field_validation_unicode_decode_error_handler():
    """Test UNICODE_DECODE_ERROR_HANDLER validation."""
    with pytest.raises(ValidationError):
        _Settings(UNICODE_DECODE_ERROR_HANDLER="invalid")

    # Valid handlers
    valid_handlers = [
        "strict",
        "ignore",
        "replace",
        "backslashreplace",
        "surrogateescape",
    ]
    for handler in valid_handlers:
        settings = _Settings(UNICODE_DECODE_ERROR_HANDLER=handler)
        assert handler == settings.UNICODE_DECODE_ERROR_HANDLER
