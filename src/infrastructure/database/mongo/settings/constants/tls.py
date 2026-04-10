from typing import Final, final


@final
class TLSDefaults:
    ENABLE: Final[bool] = False
    INSECURE: Final[bool] = False
    ALLOW_INVALID_CERTIFICATES: Final[bool] = False
    ALLOW_INVALID_HOSTNAMES: Final[bool] = False
    CA_FILE: Final[str | None] = None
    CERTIFICATE_KEY_FILE: Final[str | None] = None
    CRL_FILE: Final[str | None] = None
    CERTIFICATE_KEY_FILE_PASSWORD: Final[str | None] = None
    DISABLE_OCSP_ENDPOINT_CHECK: Final[bool] = False


@final
class TLSKeys:
    ENABLE: Final[str] = "tls"
    INSECURE: Final[str] = "tlsInsecure"
    ALLOW_INVALID_CERTIFICATES: Final[str] = "tlsAllowInvalidCertificates"
    ALLOW_INVALID_HOSTNAMES: Final[str] = "tlsAllowInvalidHostnames"
    CA_FILE: Final[str] = "tlsCAFile"
    CERTIFICATE_KEY_FILE: Final[str] = "tlsCertificateKeyFile"
    CRL_FILE: Final[str] = "tlsCRLFile"
    CERTIFICATE_KEY_FILE_PASSWORD: Final[str] = "tlsCertificateKeyFilePassword"  # noqa: S105
    DISABLE_OCSP_ENDPOINT_CHECK: Final[str] = "tlsDisableOCSPEndpointCheck"
