from pydantic import Field
from pydantic_settings import BaseSettings

from src.infra.mongo.annotations import ClientKwargsType
from src.infra.mongo.constants.settings import TLSDefaults, TLSKeys


class TLSSettings(BaseSettings):
    ENABLE: bool = Field(
        default=TLSDefaults.ENABLE,
        description="Enable TLS encryption",
    )
    INSECURE: bool = Field(
        default=TLSDefaults.INSECURE,
        description="Specify whether TLS constraints should "
        "be relaxed as much as possible",
    )
    ALLOW_INVALID_CERTIFICATES: bool = Field(
        default=TLSDefaults.ALLOW_INVALID_CERTIFICATES,
        description="Allow invalid TLS certificates",
    )
    ALLOW_INVALID_HOSTNAMES: bool = Field(
        default=TLSDefaults.ALLOW_INVALID_HOSTNAMES,
        description="Allow mismatched TLS certificate hostnames",
    )
    DISABLE_OCSP_ENDPOINT_CHECK: bool = Field(
        default=TLSDefaults.DISABLE_OCSP_ENDPOINT_CHECK,
        description="If ``True``, disables certificate revocation status "
        "checking via the OCSP responder specified on "
        "the server certificate",
    )
    CA_FILE: str | None = Field(
        default=TLSDefaults.CA_FILE,
        description="Path to custom CA file for TLS validation",
        min_length=1,
    )
    CERTIFICATE_KEY_FILE: str | None = Field(
        default=TLSDefaults.CERTIFICATE_KEY_FILE,
        description="Path to client certificate and key file",
        min_length=1,
    )
    CRL_FILE: str | None = Field(
        default=TLSDefaults.CRL_FILE,
        description="Path to file containing a PEM or DER "
        "formatted certificate revocation list",
        min_length=1,
    )
    CERTIFICATE_KEY_FILE_PASSWORD: str | None = Field(
        default=TLSDefaults.CERTIFICATE_KEY_FILE_PASSWORD,
        description="The password or passphrase for "
        "decrypting the private key in ``tlsCertificateKeyFile``. "
        "Only necessary if the private key is encrypted",
        min_length=1,
    )

    @property
    def client_kwargs(self) -> ClientKwargsType:
        """Returns a dictionary with parameters for creating an AsyncMongoClient
        instance.
        """
        d: ClientKwargsType = {}

        if self.ENABLE:
            d[TLSKeys.ENABLE] = self.ENABLE
            d[TLSKeys.INSECURE] = self.INSECURE
            d[TLSKeys.ALLOW_INVALID_CERTIFICATES] = (
                self.ALLOW_INVALID_CERTIFICATES
            )
            d[TLSKeys.ALLOW_INVALID_HOSTNAMES] = self.ALLOW_INVALID_HOSTNAMES
            d[TLSKeys.DISABLE_OCSP_ENDPOINT_CHECK] = (
                self.DISABLE_OCSP_ENDPOINT_CHECK
            )

            if self.CA_FILE:
                d[TLSKeys.CA_FILE] = self.CA_FILE
            if self.CERTIFICATE_KEY_FILE:
                d[TLSKeys.CERTIFICATE_KEY_FILE] = self.CERTIFICATE_KEY_FILE
            if self.CRL_FILE:
                d[TLSKeys.CRL_FILE] = self.CRL_FILE
            if self.CERTIFICATE_KEY_FILE_PASSWORD:
                d[TLSKeys.CERTIFICATE_KEY_FILE_PASSWORD] = (
                    self.CERTIFICATE_KEY_FILE_PASSWORD
                )

        return d
