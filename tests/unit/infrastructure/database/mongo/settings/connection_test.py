import pytest
from pydantic import SecretStr, ValidationError

from src.infrastructure.database.mongo.settings.connection import (
    ConnectionSettings,
)
from src.infrastructure.database.mongo.settings.constants import (
    ConnectionDefaults as Defaults,
)


def test_connection_settings_default(
    default_connection_settings, default_dsn
) -> None:
    """Test default values for ConnectionSettings."""
    s = default_connection_settings
    assert s.HOST == Defaults.HOST
    assert s.PORT == Defaults.PORT
    assert s.USERNAME == Defaults.USERNAME
    assert SecretStr(Defaults.PASSWORD) == s.PASSWORD
    assert s.SCHEMA == Defaults.SCHEMA
    assert s.dsn() == default_dsn


@pytest.mark.parametrize(
    ("host", "port", "username", "password", "schema"),
    [
        ("localhost", 27017, "user", "pass", "mongodb"),
        ("example.com", 27018, "admin", "secret123", "mongodb+srv"),
    ],
)
def test_connection_settings_valid(host, port, username, password, schema):
    """Test valid minimal connection settings."""
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


@pytest.mark.parametrize(
    ("host", "port", "username", "password", "schema", "dns_string"),
    [
        (
            "localhost",
            27017,
            "user",
            "pass",
            "mongodb",
            "mongodb://user:pass@localhost:27017",
        ),
        (
            "cluster.mongodb.net",
            27017,
            "admin",
            "secret",
            "mongodb+srv",
            "mongodb+srv://admin:secret@cluster.mongodb.net:27017",
        ),
        (
            "localhost",
            27017,
            "",
            "",
            "mongodb",
            "mongodb://localhost:27017",
        ),
        (
            "localhost",
            27017,
            "",
            "pass",
            "mongodb",
            "mongodb://:pass@localhost:27017",
        ),
        (
            "localhost",
            27017,
            "user",
            "",
            "mongodb",
            "mongodb://user@localhost:27017",
        ),
    ],
)
def test_connection_settings_dsn_with_secrets(  # noqa: PLR0913
    host, port, username, password, schema, dns_string
):
    """Test DSN generation with secrets visible."""
    settings = ConnectionSettings(
        HOST=host,
        PORT=port,
        USERNAME=username,
        PASSWORD=SecretStr(password),
        SCHEMA=schema,
    )
    dsn = settings.dsn(with_secret=True)
    assert str(dsn) == dns_string


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


@pytest.mark.parametrize(
    ("host", "port", "username", "password", "schema"),
    [
        ("", 27017, "user", "pass", "mongodb"),
        ("a" * 256, 27017, "user", "pass", "mongodb"),
        ("localhost", 0, "user", "pass", "mongodb"),
        ("localhost", -1, "user", "pass", "mongodb"),
        ("localhost", 65536, "user", "pass", "mongodb"),
        ("localhost", 65536, "a" * 256, "pass", "mongodb"),
        ("localhost", 65536, "user", "a" * 256, "mongodb"),
        ("localhost", 65536, "user", "pass", "invalid"),
    ],
)
def test_connection_settings_invalid_host_empty(
    host, port, username, password, schema
):
    """Test invalid empty host."""
    with pytest.raises(ValidationError):
        ConnectionSettings(
            HOST=host,
            PORT=port,
            USERNAME=username,
            PASSWORD=SecretStr(password),
            SCHEMA=schema,
        )
