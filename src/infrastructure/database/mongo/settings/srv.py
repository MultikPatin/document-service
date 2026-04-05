from typing import Any

from pydantic import Field, PositiveInt
from pydantic_settings import BaseSettings

from .defaults import SRVDefaults


class SRVSettings(BaseSettings):
    SERVICE_NAME: str = Field(
        default=SRVDefaults.SERVICE_NAME,
        description="Service name for DNS SRV lookups",
        min_length=1,
    )
    MAX_HOSTS: PositiveInt = Field(
        default=SRVDefaults.MAX_HOSTS,
        description="Maximum number of hosts to connect to with SRV",
    )

    @property
    def client_kwargs(self) -> dict[str, Any]:
        """Returns a dictionary with parameters for creating an AsyncMongoClient
        instance.
        """
        result: dict[str, Any] = {}

        result["srvServiceName"] = self.SERVICE_NAME
        result["srvMaxHosts"] = self.MAX_HOSTS

        return result
