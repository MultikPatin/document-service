from typing import Any

import pytest
from pydantic import ValidationError

from src.infrastructure.database.mongo.settings.tls import TLSSettings


def test_tls_settings_default_values(
    tls_settings_default: TLSSettings,
) -> None:
    """Test TLSSettings default values."""
    assert tls_settings_default.ENABLE is False
    assert tls_settings_default.INSECURE is False
    assert tls_settings_default.ALLOW_INVALID_CERTIFICATES is False
    assert tls_settings_default.ALLOW_INVALID_HOSTNAMES is False
    assert tls_settings_default.DISABLE_OCSP_ENDPOINT_CHECK is False
    assert tls_settings_default.CA_FILE is None
    assert tls_settings_default.CERTIFICATE_KEY_FILE is None
    assert tls_settings_default.CRL_FILE is None
    assert tls_settings_default.CERTIFICATE_KEY_FILE_PASSWORD is None


def test_tls_settings_custom_values(
    tls_settings_enabled: TLSSettings,
) -> None:
    """Test TLSSettings with custom values."""
    assert tls_settings_enabled.ENABLE is True
    assert tls_settings_enabled.INSECURE is True
    assert tls_settings_enabled.ALLOW_INVALID_CERTIFICATES is True
    assert tls_settings_enabled.ALLOW_INVALID_HOSTNAMES is True
    assert tls_settings_enabled.DISABLE_OCSP_ENDPOINT_CHECK is True
    assert tls_settings_enabled.CA_FILE == "/path/to/ca.pem"
    assert tls_settings_enabled.CERTIFICATE_KEY_FILE == "/path/to/client.pem"
    assert tls_settings_enabled.CRL_FILE == "/path/to/crl.pem"
    assert tls_settings_enabled.CERTIFICATE_KEY_FILE_PASSWORD == "secret"


@pytest.mark.parametrize(
    ("enable", "expected"),
    [
        (False, {}),
        (
            True,
            {
                "tls": True,
                "tlsInsecure": False,
                "tlsAllowInvalidCertificates": False,
                "tlsAllowInvalidHostnames": False,
                "tlsDisableOCSPEndpointCheck": False,
            },
        ),
    ],
)
def test_tls_settings_client_kwargs_tls_enable(
    tls_settings_default: TLSSettings,
    enable: bool,
    expected: dict[str, Any],
) -> None:
    """Test client_kwargs when TLS is enabled or disabled."""
    settings = TLSSettings(ENABLE=enable)
    assert settings.client_kwargs == expected


def test_tls_settings_client_kwargs_type(
    tls_settings_default: TLSSettings,
) -> None:
    """Test client_kwargs returns a dictionary."""
    assert isinstance(tls_settings_default.client_kwargs, dict)


def test_tls_settings_client_kwargs_with_files(
    tls_settings_enabled: TLSSettings,
) -> None:
    """Test client_kwargs contains file paths when TLS is enabled."""
    expected = {
        "tls": True,
        "tlsInsecure": True,
        "tlsAllowInvalidCertificates": True,
        "tlsAllowInvalidHostnames": True,
        "tlsDisableOCSPEndpointCheck": True,
        "tlsCAFile": "/path/to/ca.pem",
        "tlsCertificateKeyFile": "/path/to/client.pem",
        "tlsCRLFile": "/path/to/crl.pem",
        "tlsCertificateKeyFilePassword": "secret",
    }
    assert tls_settings_enabled.client_kwargs == expected


@pytest.mark.parametrize(
    "value",
    [
        "CA_FILE",
        "CERTIFICATE_KEY_FILE",
        "CRL_FILE",
        "CERTIFICATE_KEY_FILE_PASSWORD",
    ],
)
def test_tls_settings_string_fields_validation(value) -> None:
    """Test validation of string fields with min_length=1."""
    with pytest.raises(ValidationError):
        TLSSettings(**{value: ""})


@pytest.mark.parametrize(
    "value",
    ["not_a_bool", 123, None],
)
def test_tls_settings_invalid_types(value) -> None:
    """Test type validation for boolean fields."""
    with pytest.raises(ValidationError):
        TLSSettings(ENABLE=value)

    with pytest.raises(ValidationError):
        TLSSettings(INSECURE=value)

    with pytest.raises(ValidationError):
        TLSSettings(ALLOW_INVALID_CERTIFICATES=value)

    with pytest.raises(ValidationError):
        TLSSettings(ALLOW_INVALID_HOSTNAMES=value)

    with pytest.raises(ValidationError):
        TLSSettings(DISABLE_OCSP_ENDPOINT_CHECK=value)
