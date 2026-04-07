import pytest
from pydantic import SecretStr, ValidationError

from src.infrastructure.database.mongo.settings.connection import (
    ConnectionSettings,
)


def test_connection_settings_valid_minimal():
    """Test valid minimal connection settings."""
    host = "localhost"
    port = 27017
    username = "user"
    password = "pass"
    schema = "mongodb"
    settings = ConnectionSettings(
        HOST=host,
        PORT=port,
        USERNAME=username,
        PASSWORD=SecretStr(password),
        SCHEMA=schema,
    )
    assert host == settings.HOST
    assert port == settings.PORT
    assert username == settings.USERNAME
    assert settings.PASSWORD.get_secret_value() == password
    assert schema == settings.SCHEMA


def test_connection_settings_valid_full():
    """Test valid full connection settings with all fields."""
    host = "example.com"
    port = 27018
    username = "admin"
    password = "secret123"
    schema = "mongodb+srv"
    settings = ConnectionSettings(
        HOST=host,
        PORT=port,
        USERNAME=username,
        PASSWORD=SecretStr(password),
        SCHEMA=schema,
    )
    assert host == settings.HOST
    assert port == settings.PORT
    assert username == settings.USERNAME
    assert settings.PASSWORD.get_secret_value() == password
    assert schema == settings.SCHEMA


def test_connection_settings_invalid_host_empty():
    """Test invalid empty host."""
    with pytest.raises(ValidationError):
        ConnectionSettings(
            HOST="",
            PORT=27017,
            USERNAME="user",
            PASSWORD=SecretStr("pass"),
            SCHEMA="mongodb",
        )


def test_connection_settings_invalid_host_too_long():
    """Test invalid host with more than 255 characters."""
    long_host = "a" * 256
    with pytest.raises(ValidationError):
        ConnectionSettings(
            HOST=long_host,
            PORT=27017,
            USERNAME="user",
            PASSWORD=SecretStr("pass"),
            SCHEMA="mongodb",
        )


def test_connection_settings_invalid_port_zero():
    """Test invalid port with zero value."""
    with pytest.raises(ValidationError):
        ConnectionSettings(
            HOST="localhost",
            PORT=0,
            USERNAME="user",
            PASSWORD=SecretStr("pass"),
            SCHEMA="mongodb",
        )


def test_connection_settings_invalid_port_negative():
    """Test invalid port with negative value."""
    with pytest.raises(ValidationError):
        ConnectionSettings(
            HOST="localhost",
            PORT=-1,
            USERNAME="user",
            PASSWORD=SecretStr("pass"),
            SCHEMA="mongodb",
        )


def test_connection_settings_invalid_port_too_high():
    """Test invalid port with value greater than 65535."""
    with pytest.raises(ValidationError):
        ConnectionSettings(
            HOST="localhost",
            PORT=65536,
            USERNAME="user",
            PASSWORD=SecretStr("pass"),
            SCHEMA="mongodb",
        )


def test_connection_settings_invalid_username_too_long():
    """Test invalid username with more than 255 characters."""
    long_username = "a" * 256
    with pytest.raises(ValidationError):
        ConnectionSettings(
            HOST="localhost",
            PORT=27017,
            USERNAME=long_username,
            PASSWORD=SecretStr("pass"),
            SCHEMA="mongodb",
        )


def test_connection_settings_invalid_password_too_long():
    """Test invalid password with more than 255 characters."""
    long_password = "a" * 256
    with pytest.raises(ValidationError):
        ConnectionSettings(
            HOST="localhost",
            PORT=27017,
            USERNAME="user",
            PASSWORD=SecretStr(long_password),
            SCHEMA="mongodb",
        )


def test_connection_settings_invalid_schema():
    """Test invalid schema not in allowed values."""
    with pytest.raises(ValidationError):
        ConnectionSettings(
            HOST="localhost",
            PORT=27017,
            USERNAME="user",
            PASSWORD=SecretStr("pass"),
            SCHEMA="invalid",
        )


def test_connection_settings_dsn_with_secrets():
    """Test DSN generation with secrets visible."""
    settings = ConnectionSettings(
        HOST="localhost",
        PORT=27017,
        USERNAME="user",
        PASSWORD=SecretStr("pass"),
        SCHEMA="mongodb",
    )
    dsn = settings.dsn(with_secret=True)
    assert str(dsn) == "mongodb://user:pass@localhost:27017"


def test_connection_settings_dsn_without_secrets():
    """Test DSN generation with secrets hidden."""
    settings = ConnectionSettings(
        HOST="localhost",
        PORT=27017,
        USERNAME="user",
        PASSWORD=SecretStr("pass"),
        SCHEMA="mongodb",
    )
    dsn = settings.dsn(with_secret=False)
    assert str(dsn) == "mongodb://user:**********@localhost:27017"


def test_connection_settings_dsn_with_srv():
    """Test DSN generation with mongodb+srv schema."""
    settings = ConnectionSettings(
        HOST="cluster.mongodb.net",
        PORT=27017,
        USERNAME="admin",
        PASSWORD=SecretStr("secret"),
        SCHEMA="mongodb+srv",
    )
    dsn = settings.dsn(with_secret=True)
    assert str(dsn) == "mongodb+srv://admin:secret@cluster.mongodb.net:27017"


def test_connection_settings_dsn_without_credentials():
    """Test DSN generation without username and password."""
    settings = ConnectionSettings(
        HOST="localhost",
        PORT=27017,
        USERNAME="",
        PASSWORD=SecretStr(""),
        SCHEMA="mongodb",
    )
    dsn = settings.dsn(with_secret=True)
    assert str(dsn) == "mongodb://localhost:27017"


def test_connection_settings_dsn_edge_cases():
    """Test DSN generation edge cases."""
    # Test with empty username and non-empty password
    settings = ConnectionSettings(
        HOST="localhost",
        PORT=27017,
        USERNAME="",
        PASSWORD=SecretStr("pass"),
        SCHEMA="mongodb",
    )
    dsn = settings.dsn(with_secret=True)
    assert str(dsn) == "mongodb://:pass@localhost:27017"

    # Test with non-empty username and empty password
    settings = ConnectionSettings(
        HOST="localhost",
        PORT=27017,
        USERNAME="user",
        PASSWORD=SecretStr(""),
        SCHEMA="mongodb",
    )
    dsn = settings.dsn(with_secret=True)
    assert str(dsn) == "mongodb://user@localhost:27017"
