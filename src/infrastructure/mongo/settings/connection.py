from pydantic import Field
from pydantic_settings import BaseSettings

from libs.mongo.constants.settings import (
    ConnectionModeDefaults,
    ConnectionModeKeys,
    ConnectionModeReadPreferenceEnum,
)
from src.infrastructure.mongo.annotations import ClientKwargsType


class ConnectionSettings(BaseSettings):
    DIRECT_CONNECTION: bool | None = Field(
        default=ConnectionModeDefaults.DIRECT_CONNECTION,
        description="Direct connection to single server",
    )
    APPNAME: str | None = Field(
        default=ConnectionModeDefaults.APPNAME,
        description="Application name (visible in logs)",
        min_length=1,
        max_length=128,
    )
    READ_PREFERENCE: ConnectionModeReadPreferenceEnum | None = Field(
        default=ConnectionModeDefaults.READ_PREFERENCE,
        description="Read preference mode",
    )
    READ_PREFERENCE_TAGS: str | None = Field(
        default=ConnectionModeDefaults.READ_PREFERENCE_TAGS,
        description="Specifies a tag set as a comma-separated list "
        "of colon-separated key-value pairs",
    )
    MAX_STALENESS_SECONDS: int | None = Field(
        default=ConnectionModeDefaults.MAX_STALENESS_SECONDS,
        description="The maximum estimated length of time a replica set "
        "secondary can fall behind the primary in replication "
        "before it will no longer be selected for operations",
        ge=0,
        le=90000,
    )
    REPLICA_SET_NAME: str | None = Field(
        default=ConnectionModeDefaults.REPLICA_SET_NAME,
        description="Replica set name",
        min_length=1,
        max_length=128,
    )

    @property
    def client_kwargs(self) -> ClientKwargsType:
        """Returns a dictionary with parameters for creating an AsyncMongoClient
        instance.
        """
        d: ClientKwargsType = {}

        if self.DIRECT_CONNECTION is not None:
            d[ConnectionModeKeys.DIRECT_CONNECTION] = self.DIRECT_CONNECTION
        if self.APPNAME is not None and self.APPNAME != "":
            d[ConnectionModeKeys.APPNAME] = self.APPNAME
        if self.READ_PREFERENCE is not None:
            d[ConnectionModeKeys.READ_PREFERENCE] = self.READ_PREFERENCE.value
        if self.READ_PREFERENCE_TAGS is not None:
            d[ConnectionModeKeys.READ_PREFERENCE_TAGS] = (
                self.READ_PREFERENCE_TAGS
            )
        if self.MAX_STALENESS_SECONDS is not None:
            d[ConnectionModeKeys.MAX_STALENESS_SECONDS] = (
                self.MAX_STALENESS_SECONDS
            )
        if self.REPLICA_SET_NAME is not None and self.REPLICA_SET_NAME != "":
            d[ConnectionModeKeys.REPLICA_SET_NAME] = self.REPLICA_SET_NAME

        return d
