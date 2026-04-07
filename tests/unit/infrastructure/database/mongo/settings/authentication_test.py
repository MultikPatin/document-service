from typing import Any

import pytest
from pydantic import ValidationError

from src.infrastructure.database.mongo.settings.authentication import (
    AuthenticationSettings,
)


def test_authentication_settings_valid_scram_sha1() -> None:
    """Test valid AuthenticationSettings with SCRAM-SHA-1 mechanism."""
    source = "admin"
    mechanism = "SCRAM-SHA-1"
    settings = AuthenticationSettings(SOURCE=source, MECHANISM=mechanism)
    assert source == settings.SOURCE
    assert mechanism == settings.MECHANISM
    assert settings.client_kwargs == {
        "authSource": source,
        "authMechanism": mechanism,
    }


def test_authentication_settings_valid_scram_sha256() -> None:
    """Test valid AuthenticationSettings with SCRAM-SHA-256 mechanism."""
    source = "mydb"
    mechanism = "SCRAM-SHA-256"
    settings = AuthenticationSettings(SOURCE=source, MECHANISM=mechanism)
    assert source == settings.SOURCE
    assert mechanism == settings.MECHANISM
    assert settings.client_kwargs == {
        "authSource": source,
        "authMechanism": mechanism,
    }


def test_authentication_settings_default_values() -> None:
    """Test AuthenticationSettings with default values."""
    source = "admin"
    mechanism = "SCRAM-SHA-256"
    settings = AuthenticationSettings()
    assert source == settings.SOURCE
    assert mechanism == settings.MECHANISM
    assert settings.client_kwargs == {
        "authSource": source,
        "authMechanism": mechanism,
    }


def test_authentication_settings_source_min_length() -> None:
    """Test SOURCE field with minimum length (1 character)."""
    source = "a"
    mechanism = "SCRAM-SHA-1"
    settings = AuthenticationSettings(SOURCE=source, MECHANISM=mechanism)
    assert source == settings.SOURCE
    assert settings.client_kwargs["authSource"] == source


def test_authentication_settings_source_max_length() -> None:
    """Test SOURCE field with maximum length (64 characters)."""
    source = "a" * 64
    mechanism = "SCRAM-SHA-256"
    settings = AuthenticationSettings(SOURCE=source, MECHANISM=mechanism)
    assert source == settings.SOURCE
    assert settings.client_kwargs["authSource"] == source


def test_authentication_settings_source_too_short() -> None:
    """Test SOURCE field with empty string (invalid)."""
    source = ""
    mechanism = "SCRAM-SHA-1"
    with pytest.raises(ValidationError):
        AuthenticationSettings(SOURCE=source, MECHANISM=mechanism)


def test_authentication_settings_source_too_long() -> None:
    """Test SOURCE field with 65 characters (invalid)."""
    source = "a" * 65
    mechanism = "SCRAM-SHA-256"
    with pytest.raises(ValidationError):
        AuthenticationSettings(SOURCE=source, MECHANISM=mechanism)


def test_authentication_settings_mechanism_invalid() -> None:
    """Test MECHANISM field with invalid value."""
    source = "admin"
    mechanism = "INVALID"
    with pytest.raises(ValidationError):
        AuthenticationSettings(SOURCE=source, MECHANISM=mechanism)


def test_authentication_settings_client_kwargs_returns_dict() -> None:
    """Test client_kwargs property returns correct dictionary structure."""
    source = "testdb"
    mechanism = "SCRAM-SHA-1"
    settings = AuthenticationSettings(SOURCE=source, MECHANISM=mechanism)
    kwargs: dict[str, Any] = settings.client_kwargs
    assert isinstance(kwargs, dict)
    expected_keys = {"authSource", "authMechanism"}
    assert set(kwargs.keys()) == expected_keys


def test_authentication_settings_client_kwargs_values() -> None:
    """Test client_kwargs property returns correct values from fields."""
    source = "custom"
    mechanism = "SCRAM-SHA-256"
    settings = AuthenticationSettings(SOURCE=source, MECHANISM=mechanism)
    kwargs: dict[str, Any] = settings.client_kwargs
    assert kwargs["authSource"] == source
    assert kwargs["authMechanism"] == mechanism
