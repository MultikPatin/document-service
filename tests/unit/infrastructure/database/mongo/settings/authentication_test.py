import pytest
from pydantic import ValidationError

from src.infrastructure.database.mongo.settings.constants import (
    AuthenticationDefaults as D,
)
from src.infrastructure.database.mongo.settings.constants import (
    AuthenticationKeys as K,
)


def test_authentication_settings_default(
    default_authentication_settings, default_authentication_client_kwargs
) -> None:
    """Test default values for AuthenticationSettings."""
    s = default_authentication_settings
    assert s.SOURCE == D.SOURCE
    assert D.MECHANISM == s.MECHANISM
    assert s.client_kwargs == default_authentication_client_kwargs


@pytest.mark.parametrize(
    "kwargs",
    [
        {"MECHANISM": "SCRAM-SHA-1"},
        {"MECHANISM": "SCRAM-SHA-256"},
    ],
    ids=["scram-sha-1", "scram-sha-256"],
)
def test_authentication_settings_with_valid_mechanisms(
    custom_authentication_settings, kwargs
) -> None:
    """Test AuthenticationSettings with valid authentication mechanisms."""
    settings = custom_authentication_settings(**kwargs)

    assert kwargs["MECHANISM"] == settings.MECHANISM
    assert settings.client_kwargs == {
        K.SOURCE: D.SOURCE,
        K.MECHANISM: kwargs["MECHANISM"],
    }


@pytest.mark.parametrize(
    "kwargs",
    [
        {"SOURCE": "testdb", "MECHANISM": "SCRAM-SHA-1"},
        {"SOURCE": "testdb2", "MECHANISM": "SCRAM-SHA-256"},
    ],
    ids=["scram-sha1-custom-source", "scram-sha256-custom-source"],
)
def test_authentication_settings_with_combinations(
    custom_authentication_settings, kwargs
) -> None:
    """Test client_kwargs with various combinations of source and mechanism."""
    settings = custom_authentication_settings(**kwargs)

    assert settings.client_kwargs == {
        K.SOURCE: kwargs["SOURCE"],
        K.MECHANISM: kwargs["MECHANISM"],
    }


@pytest.mark.parametrize(
    "kwargs",
    [{"SOURCE": "a"}, {"SOURCE": "a" * 64}],
    ids=["min-source-length", "max-source-length"],
)
def test_authentication_settings_with_valid_source_string_lengths(
    custom_authentication_settings, kwargs
) -> None:
    """Test AuthenticationSettings with boundary values for SOURCE length."""
    settings = custom_authentication_settings(**kwargs)

    assert kwargs["SOURCE"] == settings.SOURCE
    assert D.MECHANISM == settings.MECHANISM
    assert settings.client_kwargs == {
        K.SOURCE: kwargs["SOURCE"],
        K.MECHANISM: D.MECHANISM,
    }


@pytest.mark.parametrize(
    "kwargs",
    [
        {"SOURCE": "a" * 65},
        {"SOURCE": ""},
        {"MECHANISM": "INVALID"},
        {"MECHANISM": ""},
    ],
    ids=[
        "too-long-source-length",
        "empty-source",
        "invalid-mechanism",
        "empty-mechanism",
    ],
)
def test_authentication_settings_validation_errors(
    custom_authentication_settings, kwargs
) -> None:
    """Test ValidationErrors"""
    with pytest.raises(ValidationError):
        custom_authentication_settings(**kwargs)
