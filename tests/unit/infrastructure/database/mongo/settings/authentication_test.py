import pytest
from pydantic import ValidationError

from src.infrastructure.database.mongo.settings.authentication import (
    AuthenticationSettings,
)


def test_authentication_settings_default_values() -> None:
    """Test default values for AuthenticationSettings."""
    settings = AuthenticationSettings()

    assert settings.SOURCE == "admin"
    assert settings.MECHANISM == "SCRAM-SHA-256"
    assert settings.client_kwargs == {
        "authSource": "admin",
        "authMechanism": "SCRAM-SHA-256",
    }


@pytest.mark.parametrize(
    ("mechanism", "expected_mechanism"),
    [
        ("SCRAM-SHA-1", "SCRAM-SHA-1"),
        ("SCRAM-SHA-256", "SCRAM-SHA-256"),
    ],
    ids=["scram-sha1", "scram-sha256"],
)
def test_authentication_settings_with_valid_mechanisms(
    mechanism: str, expected_mechanism: str
) -> None:
    """Test AuthenticationSettings with valid authentication mechanisms."""
    settings = AuthenticationSettings(MECHANISM=mechanism)

    assert settings.SOURCE == "admin"
    assert expected_mechanism == settings.MECHANISM
    assert settings.client_kwargs == {
        "authSource": "admin",
        "authMechanism": expected_mechanism,
    }


@pytest.mark.parametrize(
    ("source", "mechanism", "expected_auth_source", "expected_auth_mechanism"),
    [
        ("testdb", "SCRAM-SHA-1", "testdb", "SCRAM-SHA-1"),
        ("custom", "SCRAM-SHA-256", "custom", "SCRAM-SHA-256"),
    ],
    ids=["scram-sha1-custom-source", "scram-sha256-custom-source"],
)
def test_authentication_settings_client_kwargs_with_combinations(
    source: str,
    mechanism: str,
    expected_auth_source: str,
    expected_auth_mechanism: str,
) -> None:
    """Test client_kwargs with various combinations of source and mechanism."""
    settings = AuthenticationSettings(SOURCE=source, MECHANISM=mechanism)

    assert settings.client_kwargs == {
        "authSource": expected_auth_source,
        "authMechanism": expected_auth_mechanism,
    }


@pytest.mark.parametrize(
    "source_length",
    [1, 64],
)
def test_authentication_settings_with_boundary_source_lengths(
    source_length: int,
) -> None:
    """Test AuthenticationSettings with boundary values for SOURCE length."""
    source = "a" * source_length
    settings = AuthenticationSettings(SOURCE=source)

    assert source == settings.SOURCE
    assert settings.MECHANISM == "SCRAM-SHA-256"
    assert settings.client_kwargs == {
        "authSource": source,
        "authMechanism": "SCRAM-SHA-256",
    }


def test_authentication_settings_validation_error_too_long_source() -> None:
    """Test ValidationError for SOURCE longer than 64 characters."""
    long_source = "a" * 65
    with pytest.raises(ValidationError):
        AuthenticationSettings(SOURCE=long_source)


def test_authentication_settings_validation_error_empty_source() -> None:
    """Test ValidationError for empty SOURCE."""
    with pytest.raises(ValidationError):
        AuthenticationSettings(SOURCE="")


def test_authentication_settings_validation_error_invalid_mechanism() -> None:
    """Test ValidationError for invalid MECHANISM."""
    with pytest.raises(ValidationError):
        AuthenticationSettings(MECHANISM="INVALID")


def test_authentication_settings_validation_error_empty_mechanism() -> None:
    """Test ValidationError for empty MECHANISM."""
    with pytest.raises(ValidationError):
        AuthenticationSettings(MECHANISM="")
