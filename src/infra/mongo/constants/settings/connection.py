from enum import StrEnum
from typing import Final, final


class ConnectionModeReadPreferenceEnum(StrEnum):
    primary = "primary"
    secondary = "secondary"
    primary_preferred = "primaryPreferred"
    secondary_preferred = "secondaryPreferred"
    nearest = "nearest"


@final
class ConnectionDefaults:
    DIRECT_CONNECTION: Final[bool | None] = None
    APPNAME: Final[str | None] = None
    READ_PREFERENCE: Final[ConnectionModeReadPreferenceEnum | None] = None
    READ_PREFERENCE_TAGS: Final[str | None] = None
    MAX_STALENESS_SECONDS: Final[int | None] = None
    REPLICA_SET_NAME: Final[str | None] = None


@final
class ConnectionKeys:
    DIRECT_CONNECTION = "directConnection"
    APPNAME = "appname"
    READ_PREFERENCE = "readPreference"
    READ_PREFERENCE_TAGS = "readPreferenceTags"
    MAX_STALENESS_SECONDS = "maxStalenessSeconds"
    REPLICA_SET_NAME = "replicaSet"
