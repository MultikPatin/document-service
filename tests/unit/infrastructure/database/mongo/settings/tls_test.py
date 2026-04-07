from typing import Any

import pytest
from pydantic import ValidationError

from src.infrastructure.database.mongo.settings.constants import TLSDefaults
from src.infrastructure.database.mongo.settings.tls import TLSSettings


def test_tls_settings_defaults() -> None:
    """Test that TLSSettings uses correct default values."""
    enable = TLSDefaults.ENABLE
    insecure = TLSDefaults.INSECURE
    allow_invalid_certificates = TLSDefaults.ALLOW_INVALID_CERTIFICATES
    allow_invalid_hostnames = TLSDefaults.ALLOW_INVALID_HOSTNAMES
    disable_ocsp_endpoint_check = TLSDefaults.DISABLE_OCSP_ENDPOINT_CHECK
    ca_file = TLSDefaults.CA_FILE
    certificate_key_file = TLSDefaults.CERTIFICATE_KEY_FILE
    crl_file = TLSDefaults.CRL_FILE
    certificate_key_file_password = TLSDefaults.CERTIFICATE_KEY_FILE_PASSWORD

    settings = TLSSettings()

    assert enable is settings.ENABLE
    assert insecure is settings.INSECURE
    assert allow_invalid_certificates is settings.ALLOW_INVALID_CERTIFICATES
    assert allow_invalid_hostnames is settings.ALLOW_INVALID_HOSTNAMES
    assert disable_ocsp_endpoint_check is settings.DISABLE_OCSP_ENDPOINT_CHECK
    assert ca_file is settings.CA_FILE
    assert certificate_key_file is settings.CERTIFICATE_KEY_FILE
    assert crl_file is settings.CRL_FILE
    assert (
        certificate_key_file_password is settings.CERTIFICATE_KEY_FILE_PASSWORD
    )


def test_tls_settings_custom_values() -> None:
    """Test that TLSSettings properly sets custom values for all fields."""
    enable = True
    insecure = True
    allow_invalid_certificates = True
    allow_invalid_hostnames = True
    disable_ocsp_endpoint_check = True
    ca_file = "/path/to/ca.pem"
    certificate_key_file = "/path/to/client.pem"
    crl_file = "/path/to/crl.pem"
    certificate_key_file_password = "secret"

    settings = TLSSettings(
        ENABLE=enable,
        INSECURE=insecure,
        ALLOW_INVALID_CERTIFICATES=allow_invalid_certificates,
        ALLOW_INVALID_HOSTNAMES=allow_invalid_hostnames,
        DISABLE_OCSP_ENDPOINT_CHECK=disable_ocsp_endpoint_check,
        CA_FILE=ca_file,
        CERTIFICATE_KEY_FILE=certificate_key_file,
        CRL_FILE=crl_file,
        CERTIFICATE_KEY_FILE_PASSWORD=certificate_key_file_password,
    )

    assert enable is settings.ENABLE
    assert insecure is settings.INSECURE
    assert allow_invalid_certificates is settings.ALLOW_INVALID_CERTIFICATES
    assert allow_invalid_hostnames is settings.ALLOW_INVALID_HOSTNAMES
    assert disable_ocsp_endpoint_check is settings.DISABLE_OCSP_ENDPOINT_CHECK
    assert ca_file == settings.CA_FILE
    assert certificate_key_file == settings.CERTIFICATE_KEY_FILE
    assert crl_file == settings.CRL_FILE
    assert (
        certificate_key_file_password == settings.CERTIFICATE_KEY_FILE_PASSWORD
    )


def test_tls_settings_client_kwargs_enabled() -> None:
    """Test that client_kwargs returns correct dictionary when TLS is enabled."""
    enable = True
    insecure = True
    allow_invalid_certificates = True
    allow_invalid_hostnames = True
    disable_ocsp_endpoint_check = True
    ca_file = "/path/to/ca.pem"
    certificate_key_file = "/path/to/client.pem"
    crl_file = "/path/to/crl.pem"
    certificate_key_file_password = "secret"

    settings = TLSSettings(
        ENABLE=enable,
        INSECURE=insecure,
        ALLOW_INVALID_CERTIFICATES=allow_invalid_certificates,
        ALLOW_INVALID_HOSTNAMES=allow_invalid_hostnames,
        DISABLE_OCSP_ENDPOINT_CHECK=disable_ocsp_endpoint_check,
        CA_FILE=ca_file,
        CERTIFICATE_KEY_FILE=certificate_key_file,
        CRL_FILE=crl_file,
        CERTIFICATE_KEY_FILE_PASSWORD=certificate_key_file_password,
    )

    kwargs: dict[str, Any] = settings.client_kwargs
    assert isinstance(kwargs, dict)
    assert kwargs["tls"] is enable
    assert kwargs["tlsInsecure"] is insecure
    assert kwargs["tlsAllowInvalidCertificates"] is allow_invalid_certificates
    assert kwargs["tlsAllowInvalidHostnames"] is allow_invalid_hostnames
    assert kwargs["tlsDisableOCSPEndpointCheck"] is disable_ocsp_endpoint_check
    assert kwargs["tlsCAFile"] == ca_file
    assert kwargs["tlsCertificateKeyFile"] == certificate_key_file
    assert kwargs["tlsCRLFile"] == crl_file
    assert (
        kwargs["tlsCertificateKeyFilePassword"] == certificate_key_file_password
    )


def test_tls_settings_client_kwargs_disabled() -> None:
    """Test that client_kwargs returns empty dict when TLS is disabled."""
    enable = False
    settings = TLSSettings(ENABLE=enable)
    kwargs: dict[str, Any] = settings.client_kwargs
    assert isinstance(kwargs, dict)
    assert len(kwargs) == 0


def test_tls_settings_client_kwargs_type() -> None:
    """Test that client_kwargs returns a dictionary type."""
    settings = TLSSettings()
    kwargs: dict[str, Any] = settings.client_kwargs
    assert isinstance(kwargs, dict)


def test_tls_settings_string_field_min_length() -> None:
    """Test that string fields enforce minimum length of 1 character."""
    # Test CA_FILE with empty string
    with pytest.raises(ValidationError):
        TLSSettings(CA_FILE="")

    # Test CERTIFICATE_KEY_FILE with empty string
    with pytest.raises(ValidationError):
        TLSSettings(CERTIFICATE_KEY_FILE="")

    # Test CRL_FILE with empty string
    with pytest.raises(ValidationError):
        TLSSettings(CRL_FILE="")

    # Test CERTIFICATE_KEY_FILE_PASSWORD with empty string
    with pytest.raises(ValidationError):
        TLSSettings(CERTIFICATE_KEY_FILE_PASSWORD="")

    # Test with single character (valid)
    ca_file = "a"
    certificate_key_file = "b"
    crl_file = "c"
    certificate_key_file_password = "d"

    settings = TLSSettings(
        CA_FILE=ca_file,
        CERTIFICATE_KEY_FILE=certificate_key_file,
        CRL_FILE=crl_file,
        CERTIFICATE_KEY_FILE_PASSWORD=certificate_key_file_password,
    )
    assert ca_file == settings.CA_FILE
    assert certificate_key_file == settings.CERTIFICATE_KEY_FILE
    assert crl_file == settings.CRL_FILE
    assert (
        certificate_key_file_password == settings.CERTIFICATE_KEY_FILE_PASSWORD
    )


def test_tls_settings_client_kwargs_optional_files_excluded() -> None:
    """Test that optional TLS file parameters are excluded from client_kwargs when None."""
    enable = True
    insecure = False
    allow_invalid_certificates = False
    allow_invalid_hostnames = False
    disable_ocsp_endpoint_check = False
    ca_file = None
    certificate_key_file = None
    crl_file = None
    certificate_key_file_password = None

    settings = TLSSettings(
        ENABLE=enable,
        INSECURE=insecure,
        ALLOW_INVALID_CERTIFICATES=allow_invalid_certificates,
        ALLOW_INVALID_HOSTNAMES=allow_invalid_hostnames,
        DISABLE_OCSP_ENDPOINT_CHECK=disable_ocsp_endpoint_check,
        CA_FILE=ca_file,
        CERTIFICATE_KEY_FILE=certificate_key_file,
        CRL_FILE=crl_file,
        CERTIFICATE_KEY_FILE_PASSWORD=certificate_key_file_password,
    )

    kwargs: dict[str, Any] = settings.client_kwargs
    assert "tlsCAFile" not in kwargs
    assert "tlsCertificateKeyFile" not in kwargs
    assert "tlsCRLFile" not in kwargs
    assert "tlsCertificateKeyFilePassword" not in kwargs


def test_tls_settings_client_kwargs_password_included_only_when_set() -> None:
    """Test that CERTIFICATE_KEY_FILE_PASSWORD is only included in client_kwargs when not None."""
    enable = True
    certificate_key_file = "/path/to/client.pem"
    certificate_key_file_password = "secret"

    # Test without password
    settings_without_password = TLSSettings(
        ENABLE=enable,
        CERTIFICATE_KEY_FILE=certificate_key_file,
        CERTIFICATE_KEY_FILE_PASSWORD=None,
    )
    kwargs_without: dict[str, Any] = settings_without_password.client_kwargs
    assert "tlsCertificateKeyFilePassword" not in kwargs_without

    # Test with password
    settings_with_password = TLSSettings(
        ENABLE=enable,
        CERTIFICATE_KEY_FILE=certificate_key_file,
        CERTIFICATE_KEY_FILE_PASSWORD=certificate_key_file_password,
    )
    kwargs_with: dict[str, Any] = settings_with_password.client_kwargs
    assert "tlsCertificateKeyFilePassword" in kwargs_with
    assert (
        kwargs_with["tlsCertificateKeyFilePassword"]
        == certificate_key_file_password
    )
