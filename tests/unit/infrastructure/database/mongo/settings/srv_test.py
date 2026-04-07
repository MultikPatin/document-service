import pytest
from pydantic import ValidationError

from src.infrastructure.database.mongo.settings.srv import (
    SRVDefaults,
    SRVSettings,
)


def test_srv_settings_default_values() -> None:
    """Test that SRVSettings uses default values from SRVDefaults when no values are provided."""
    settings = SRVSettings()

    assert settings.SERVICE_NAME == SRVDefaults.SERVICE_NAME
    assert settings.MAX_HOSTS == SRVDefaults.MAX_HOSTS


def test_srv_settings_custom_values() -> None:
    """Test that SRVSettings properly sets custom values for SERVICE_NAME and MAX_HOSTS."""
    custom_service_name = "customService"
    custom_max_hosts = 15

    settings = SRVSettings(
        SERVICE_NAME=custom_service_name, MAX_HOSTS=custom_max_hosts
    )

    assert custom_service_name == settings.SERVICE_NAME
    assert custom_max_hosts == settings.MAX_HOSTS


def test_srv_settings_client_kwargs_returns_dict() -> None:
    """Test that client_kwargs property returns a dictionary."""
    settings = SRVSettings()

    assert isinstance(settings.client_kwargs, dict)


def test_srv_settings_client_kwargs_structure() -> None:
    """Test that client_kwargs property returns dictionary with correct structure and values."""
    custom_service_name = "customService"
    custom_max_hosts = 15

    settings = SRVSettings(
        SERVICE_NAME=custom_service_name, MAX_HOSTS=custom_max_hosts
    )

    expected_kwargs = {
        "srvServiceName": custom_service_name,
        "srvMaxHosts": custom_max_hosts,
    }

    assert settings.client_kwargs == expected_kwargs


def test_srv_settings_client_kwargs_with_defaults() -> None:
    """Test that client_kwargs property returns correct values when using defaults."""
    settings = SRVSettings()

    expected_kwargs = {
        "srvServiceName": SRVDefaults.SERVICE_NAME,
        "srvMaxHosts": SRVDefaults.MAX_HOSTS,
    }

    assert settings.client_kwargs == expected_kwargs


def test_srv_settings_service_name_minimum_length() -> None:
    """Test that SERVICE_NAME validation enforces minimum length of 1 character."""
    # Test single character (valid)
    settings = SRVSettings(SERVICE_NAME="a")
    assert settings.SERVICE_NAME == "a"

    # Test empty string (invalid)
    with pytest.raises(ValidationError):
        SRVSettings(SERVICE_NAME="")


def test_srv_settings_max_hosts_positive_integer() -> None:
    """Test that MAX_HOSTS validation accepts positive integers."""
    # Test various positive integers
    for value in [1, 5, 100]:
        settings = SRVSettings(MAX_HOSTS=value)
        assert value == settings.MAX_HOSTS


def test_srv_settings_max_hosts_invalid_values() -> None:
    """Test that MAX_HOSTS validation rejects zero and negative values."""
    # Test zero
    with pytest.raises(ValidationError):
        SRVSettings(MAX_HOSTS=0)

    # Test negative values
    with pytest.raises(ValidationError):
        SRVSettings(MAX_HOSTS=-1)

    with pytest.raises(ValidationError):
        SRVSettings(MAX_HOSTS=-10)
