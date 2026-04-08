import pytest
from pydantic import ValidationError

from src.infrastructure.database.mongo.settings.composite import Settings
from src.infrastructure.database.mongo.settings.constants import (
    BaseDefaults,
)


def test_settings_uses_correct_model_config() -> None:
    """Test that Settings uses correct model_config from BaseDefaults."""

    # Check that model_config has the correct values from BaseDefaults
    settings = Settings()
    config = settings.model_config
    assert config["env_file"] == BaseDefaults.ENV_FILE
    assert config["env_prefix"] == BaseDefaults.ENV_PREFIX
    assert config["env_file_encoding"] == BaseDefaults.ENV_FILE_ENCODING
    assert config["env_nested_delimiter"] == BaseDefaults.ENV_NESTED_DELIMITER
    assert config["extra"] == BaseDefaults.EXTRA
    assert config["frozen"] == BaseDefaults.FROZEN


def test_db_name_validation_min_length() -> None:
    """Test DB_NAME field with minimum length (1 character)."""
    db_name = "a"
    settings = Settings(DB_NAME=db_name)
    assert db_name == settings.DB_NAME


def test_db_name_validation_max_length() -> None:
    """Test DB_NAME field with maximum length (32 characters)."""
    db_name = "a" * 32
    settings = Settings(DB_NAME=db_name)
    assert db_name == settings.DB_NAME


def test_database_property_returns_db_name() -> None:
    """Test that database property returns DB_NAME value."""
    db_name = "testdb"
    settings = Settings(DB_NAME=db_name)
    assert settings.database == db_name


@pytest.mark.parametrize(
    ("test_username", "test_password"),
    [
        ("", ""),
        ("past6", "secret6"),
        ("testuser", "testpass"),
    ],
)
def test_get_connections_with_secret(
    mock_connection_settings,
    test_username,
    test_password,
) -> None:
    """Test that get_connections method works with with_secret=True."""
    mock_connection_settings.USERNAME = test_username
    mock_connection_settings.PASSWORD = test_password
    url = f"mongodb://{test_username}:{test_password}@localhost:27017"
    mock_connection_settings.dsn.return_value.encoded_string.return_value = url

    settings = Settings()
    settings.__dict__["connection0"] = mock_connection_settings
    connections = settings.get_connections(with_secret=True)

    assert isinstance(connections, list)
    assert len(connections) == 1
    assert connections[0] == url
    mock_connection_settings.dsn.assert_called_once_with(with_secret=True)


def test_client_kwargs_combines_all_component_settings(  # noqa: PLR0913
    mock_pool_settings,
    mock_timeouts_settings,
    mock_retry_behavior_settings,
    mock_tls_settings,
    mock_compression_settings,
    mock_representation_settings,
    mock_connection_mode_settings,
    mock_write_concern_settings,
    mock_read_concern_settings,
    mock_error_handling_settings,
) -> None:
    """Test that client_kwargs property combines all component settings correctly."""
    settings = Settings()
    settings.__dict__["pool"] = mock_pool_settings
    settings.__dict__["timeouts"] = mock_timeouts_settings
    settings.__dict__["retry_behavior"] = mock_retry_behavior_settings
    settings.__dict__["tls"] = mock_tls_settings
    settings.__dict__["compression"] = mock_compression_settings
    settings.__dict__["representation"] = mock_representation_settings
    settings.__dict__["connection_mode"] = mock_connection_mode_settings
    settings.__dict__["write_concern"] = mock_write_concern_settings
    settings.__dict__["read_concern"] = mock_read_concern_settings
    settings.__dict__["error_handling"] = mock_error_handling_settings

    kwargs = settings.client_kwargs

    expected_keys = {
        "maxPoolSize",
        "serverSelectionTimeoutMS",
        "retryWrites",
        "tls",
        "compressors",
        "uuidRepresentation",
        "replicaSet",
        "w",
        "readConcernLevel",
    }
    assert expected_keys.issubset(kwargs.keys())
    assert kwargs["maxPoolSize"] == mock_pool_settings.MAX_SIZE
    assert (
        kwargs["serverSelectionTimeoutMS"]
        == mock_timeouts_settings.SERVER_SELECTION_MS
    )
    assert kwargs["retryWrites"] == mock_retry_behavior_settings.WRITES
    assert kwargs["tls"] == mock_tls_settings.ENABLE
    assert kwargs["compressors"] == mock_compression_settings.COMPRESSORS
    assert kwargs["uuidRepresentation"] == mock_representation_settings.UUID
    assert (
        kwargs["replicaSet"] == mock_connection_mode_settings.REPLICA_SET_NAME
    )
    assert kwargs["w"] == mock_write_concern_settings.W
    assert kwargs["readConcernLevel"] == mock_read_concern_settings.LEVEL


@pytest.mark.parametrize(
    "username",
    ["testuser", None],
)
def test_client_kwargs_includes_authentication_when_username_present(
    mock_connection_settings, mock_authentication_settings, username
) -> None:
    """Test that client_kwargs includes authentication settings when connection has USERNAME."""
    mock_connection_settings.USERNAME = username

    settings = Settings()
    settings.__dict__["connection0"] = mock_connection_settings
    settings.__dict__["authentication"] = mock_authentication_settings
    kwargs = settings.client_kwargs

    if username:
        assert "authSource" in kwargs
        assert "authMechanism" in kwargs
        assert kwargs["authSource"] == "admin"
        assert kwargs["authMechanism"] == "SCRAM-SHA-256"
    else:
        assert "authSource" not in kwargs
        assert "authMechanism" not in kwargs


@pytest.mark.parametrize(
    "schema",
    ["mongodb+srv", "mongodb"],
)
def test_client_kwargs_includes_srv_when_schema_ends_with_srv(
    mock_connection_settings, mock_srv_settings, schema
) -> None:
    """Test that client_kwargs includes srv settings when connection schema ends with 'srv'."""
    mock_connection_settings.SCHEMA = schema

    settings = Settings()
    settings.__dict__["connection0"] = mock_connection_settings
    settings.__dict__["srv"] = mock_srv_settings
    kwargs = settings.client_kwargs

    if schema.endswith("srv"):
        assert "srvServiceName" in kwargs
        assert kwargs["srvServiceName"] == "mongodb"
    else:
        assert "srvServiceName" not in kwargs


def test_db_name_validation_too_long() -> None:
    """Test DB_NAME field with 33 characters (invalid)."""
    db_name = "a" * 33
    with pytest.raises(ValidationError):
        Settings(DB_NAME=db_name)


def test_db_name_validation_too_short() -> None:
    """Test DB_NAME field with empty string (invalid)."""
    db_name = ""
    with pytest.raises(ValidationError):
        Settings(DB_NAME=db_name)
