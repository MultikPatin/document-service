from pydantic import Field, PositiveInt
from pydantic_settings import BaseSettings

from src.infrastructure.mongo.annotations import ClientKwargsType
from src.infrastructure.mongo.constants.settings import SRVDefaults, SRVKeys


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
    def client_kwargs(self) -> ClientKwargsType:
        """Returns a dictionary with parameters for creating an AsyncMongoClient
        instance.
        """
        d: ClientKwargsType = {
            SRVKeys.SERVICE_NAME: self.SERVICE_NAME,
            SRVKeys.MAX_HOSTS: self.MAX_HOSTS,
        }

        return d
