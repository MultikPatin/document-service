from unittest.mock import Mock

import pytest

from src.infrastructure.database.mongo.settings.constants import (
    ConnectionSchemaEnum,
)


@pytest.fixture
def mock_authentication_settings() -> Mock:
    """Fixture for AuthenticationSettings mock."""
    mock = Mock()
    mock.SOURCE = "admin"
    mock.MECHANISM = "SCRAM-SHA-256"
    mock.client_kwargs = {
        "authSource": "admin",
        "authMechanism": "SCRAM-SHA-256",
    }
    return mock


@pytest.fixture
def mock_compression_settings() -> Mock:
    """Fixture for CompressionSettings mock."""
    mock = Mock()
    mock.COMPRESSORS = "zlib"
    mock.client_kwargs = {"compressors": "zlib"}
    return mock


@pytest.fixture
def mock_connection_settings() -> Mock:
    """Fixture for ConnectionSettings mock."""
    mock = Mock()
    mock.USERNAME = ""
    mock.SCHEMA = ConnectionSchemaEnum.mongodb
    dsn_mock = Mock()
    dsn_mock.encoded_string.return_value = "mongodb://localhost:27017"
    mock.dsn.return_value = dsn_mock
    mock.dsn.side_effect = lambda with_secret=False: dsn_mock
    return mock


@pytest.fixture
def mock_connection_mode_settings() -> Mock:
    """Fixture for ConnectionModeSettings mock."""
    mock = Mock()
    mock.REPLICA_SET_NAME = "rs0"
    mock.client_kwargs = {"replicaSet": "rs0"}
    return mock


@pytest.fixture
def mock_error_handling_settings() -> Mock:
    """Fixture for ErrorHandlingSettings mock."""
    mock = Mock()
    mock.client_kwargs = {"serverSelectionTimeoutMS": 30000}
    return mock


@pytest.fixture
def mock_pool_settings() -> Mock:
    """Fixture for PoolSettings mock."""
    mock = Mock()
    mock.MAX_SIZE = 100
    mock.client_kwargs = {"maxPoolSize": 100}
    return mock


@pytest.fixture
def mock_read_concern_settings() -> Mock:
    """Fixture for ReadConcernSettings mock."""
    mock = Mock()
    mock.LEVEL = "majority"
    mock.client_kwargs = {"readConcernLevel": "majority"}
    return mock


@pytest.fixture
def mock_representation_settings() -> Mock:
    """Fixture for RepresentationSettings mock."""
    mock = Mock()
    mock.UUID = "standard"
    mock.client_kwargs = {"uuidRepresentation": "standard"}
    return mock


@pytest.fixture
def mock_retry_behavior_settings() -> Mock:
    """Fixture for RetryBehaviorSettings mock."""
    mock = Mock()
    mock.WRITES = True
    mock.client_kwargs = {"retryWrites": True}
    return mock


@pytest.fixture
def mock_srv_settings() -> Mock:
    """Fixture for SRVSettings mock."""
    mock = Mock()
    mock.client_kwargs = {"srvServiceName": "mongodb"}
    return mock


@pytest.fixture
def mock_timeouts_settings() -> Mock:
    """Fixture for TimeoutsSettings mock."""
    mock = Mock()
    mock.SERVER_SELECTION_MS = 30000
    mock.client_kwargs = {"serverSelectionTimeoutMS": 30000}
    return mock


@pytest.fixture
def mock_tls_settings() -> Mock:
    """Fixture for TLSSettings mock."""
    mock = Mock()
    mock.ENABLE = True
    mock.client_kwargs = {"tls": True}
    return mock


@pytest.fixture
def mock_write_concern_settings() -> Mock:
    """Fixture for WriteConcernSettings mock."""
    mock = Mock()
    mock.W = "majority"
    mock.client_kwargs = {"w": "majority"}
    return mock
