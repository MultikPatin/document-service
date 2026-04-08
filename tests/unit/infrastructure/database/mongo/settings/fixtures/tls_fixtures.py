import pytest

from src.infrastructure.database.mongo.settings.tls import TLSSettings


@pytest.fixture
def tls_settings_default() -> TLSSettings:
    """Returns a TLSSettings instance with default values."""
    return TLSSettings()


@pytest.fixture
def tls_settings_enabled() -> TLSSettings:
    """Returns a TLSSettings instance with TLS enabled and custom values."""
    return TLSSettings(
        ENABLE=True,
        INSECURE=True,
        ALLOW_INVALID_CERTIFICATES=True,
        ALLOW_INVALID_HOSTNAMES=True,
        DISABLE_OCSP_ENDPOINT_CHECK=True,
        CA_FILE="/path/to/ca.pem",
        CERTIFICATE_KEY_FILE="/path/to/client.pem",
        CRL_FILE="/path/to/crl.pem",
        CERTIFICATE_KEY_FILE_PASSWORD="secret",
    )
