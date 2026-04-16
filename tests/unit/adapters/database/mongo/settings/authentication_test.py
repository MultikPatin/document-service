import pytest
from libs.mongo.constants.settings import (
    AuthenticationDefaults as D,
)
from libs.mongo.constants.settings import (
    AuthenticationKeys as K,
)
from pydantic import ValidationError


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
    s = custom_authentication_settings(**kwargs)

    assert kwargs["MECHANISM"] == s.MECHANISM
    assert s.client_kwargs == {
        K.SOURCE: D.SOURCE,
        K.MECHANISM: kwargs["MECHANISM"],
    }


@pytest.mark.parametrize(
    "kwargs",
    [
        {"SOURCE": "testdb"},
        {"SOURCE": "a"},
        {"SOURCE": "a" * 64},
    ],
    ids=[
        "custom-source",
        "min-source-length",
        "max-source-length",
    ],
)
def test_authentication_settings_with_valid_source(
    custom_authentication_settings, kwargs
) -> None:
    """Test client_kwargs with various combinations of source and mechanism."""
    s = custom_authentication_settings(**kwargs)

    assert kwargs["SOURCE"] == s.SOURCE
    assert s.client_kwargs == {
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
