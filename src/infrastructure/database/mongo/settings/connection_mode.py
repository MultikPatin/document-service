from typing import Any

from pydantic import Field
from pydantic_settings import BaseSettings

from .constants import ConnectionModeDefaults


class ConnectionModeSettings(BaseSettings):
    DIRECT_CONNECTION: bool | None = Field(
        default=ConnectionModeDefaults.DIRECT_CONNECTION,
        description="Direct connection to single server",
    )
    APPNAME: str | None = Field(
        default=ConnectionModeDefaults.APPNAME,
        description="Application name (visible in logs)",
        max_length=128,
    )
    READ_PREFERENCE: str | None = Field(
        default=ConnectionModeDefaults.READ_PREFERENCE,
        description="Read preference mode",
        pattern="^(primary|primaryPreferred|secondary|secondaryPreferred|nearest)$",
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
    def client_kwargs(self) -> dict[str, Any]:
        """Returns a dictionary with parameters for creating an AsyncMongoClient
        instance.
        """
        result: dict[str, Any] = {}

        if self.APPNAME is not None and self.APPNAME != "":
            result["appname"] = self.APPNAME
        if self.DIRECT_CONNECTION is not None:
            result["directConnection"] = self.DIRECT_CONNECTION
        if self.READ_PREFERENCE is not None:
            result["readPreference"] = self.READ_PREFERENCE
        if self.READ_PREFERENCE_TAGS is not None:
            result["readPreferenceTags"] = self.READ_PREFERENCE_TAGS
        if self.MAX_STALENESS_SECONDS is not None:
            result["maxStalenessSeconds"] = self.MAX_STALENESS_SECONDS
        if self.REPLICA_SET_NAME is not None and self.REPLICA_SET_NAME != "":
            result["replicaSet"] = self.REPLICA_SET_NAME

        return result
