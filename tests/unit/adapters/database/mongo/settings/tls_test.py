from typing import Any

import pytest
from libs.mongo.constants.settings import (
    TLSDefaults as D,
)
from libs.mongo.settings.tls import TLSSettings
from pydantic import ValidationError


def test_tls_settings_default(
    default_tls_settings, default_tls_client_kwargs
) -> None:
    """Test default values for TLSSettings."""
    s = default_tls_settings

    assert s.ENABLE == D.ENABLE
    assert s.INSECURE == D.INSECURE
    assert s.ALLOW_INVALID_CERTIFICATES == D.ALLOW_INVALID_CERTIFICATES
    assert s.ALLOW_INVALID_HOSTNAMES == D.ALLOW_INVALID_HOSTNAMES
    assert s.DISABLE_OCSP_ENDPOINT_CHECK == D.DISABLE_OCSP_ENDPOINT_CHECK
    assert s.CA_FILE == D.CA_FILE
    assert s.CERTIFICATE_KEY_FILE == D.CERTIFICATE_KEY_FILE
    assert s.CRL_FILE == D.CRL_FILE
    assert s.CERTIFICATE_KEY_FILE_PASSWORD == D.CERTIFICATE_KEY_FILE_PASSWORD
    assert s.client_kwargs == default_tls_client_kwargs


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
