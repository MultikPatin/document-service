import pytest
from pydantic import ValidationError

from src.infrastructure.database.mongo.settings.srv import (
    SRVDefaults,
    SRVSettings,
)


def test_srv_settings_default_values(
    default_srv_settings, default_srv_client_kwargs
) -> None:
    """Test that SRVSettings uses default values from SRVDefaults when no values are provided."""
    assert default_srv_settings.SERVICE_NAME == SRVDefaults.SERVICE_NAME
    assert default_srv_settings.MAX_HOSTS == SRVDefaults.MAX_HOSTS
    assert default_srv_settings.client_kwargs == default_srv_client_kwargs


def test_srv_settings_custom_values(custom_srv_settings) -> None:
    """Test that SRVSettings properly sets custom values for SERVICE_NAME and MAX_HOSTS."""
    name = "customService"
    max_hosts = 15
    kwargs = {"SERVICE_NAME": name, "MAX_HOSTS": max_hosts}

    settings = custom_srv_settings(**kwargs)

    assert name == settings.SERVICE_NAME
    assert max_hosts == settings.MAX_HOSTS


def test_srv_settings_client_kwargs_returns_dict(
    default_srv_settings: SRVSettings,
) -> None:
    """Test that client_kwargs property returns a dictionary."""
    assert isinstance(default_srv_settings.client_kwargs, dict)


@pytest.mark.parametrize(
    ("service_name", "max_hosts"),
    [
        ("service1", 1),
        ("myService", 5),
        ("test", 100),
        ("a", 1),  # minimum valid values
    ],
)
def test_srv_settings_client_kwargs_structure_with_various_values(
    service_name: str, max_hosts: int
) -> None:
    """Test that client_kwargs property returns dictionary with correct structure and values for various inputs."""
    settings = SRVSettings(SERVICE_NAME=service_name, MAX_HOSTS=max_hosts)

    expected_kwargs = {
        "srvServiceName": service_name,
        "srvMaxHosts": max_hosts,
    }

    assert settings.client_kwargs == expected_kwargs


def test_srv_settings_client_kwargs_with_defaults(
    default_srv_settings: SRVSettings,
) -> None:
    """Test that client_kwargs property returns correct values when using defaults."""
    expected_kwargs = {
        "srvServiceName": SRVDefaults.SERVICE_NAME,
        "srvMaxHosts": SRVDefaults.MAX_HOSTS,
    }

    assert default_srv_settings.client_kwargs == expected_kwargs


@pytest.mark.parametrize(
    "service_name",
    ["a", "service", "my_service_123"],
)
def test_srv_settings_service_name_valid_values(service_name: str) -> None:
    """Test that SERVICE_NAME validation accepts various valid values."""
    settings = SRVSettings(SERVICE_NAME=service_name)
    assert service_name == settings.SERVICE_NAME


@pytest.mark.parametrize(
    "max_hosts",
    [1, 5, 100, 1000],
)
def test_srv_settings_max_hosts_valid_values(max_hosts: int) -> None:
    """Test that MAX_HOSTS validation accepts various positive integers."""
    settings = SRVSettings(MAX_HOSTS=max_hosts)
    assert max_hosts == settings.MAX_HOSTS


@pytest.mark.parametrize(
    "service_name",
    [""],
)
def test_srv_settings_service_name_invalid_values(service_name: str) -> None:
    """Test that SERVICE_NAME validation raises ValidationError for empty strings and whitespace-only values."""
    with pytest.raises(ValidationError):
        SRVSettings(SERVICE_NAME=service_name)


@pytest.mark.parametrize(
    "max_hosts",
    [0, -1, -5, -100],
)
def test_srv_settings_max_hosts_invalid_values(max_hosts: int) -> None:
    """Test that MAX_HOSTS validation raises ValidationError for non-positive values."""
    with pytest.raises(ValidationError):
        SRVSettings(MAX_HOSTS=max_hosts)
