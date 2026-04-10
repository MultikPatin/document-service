from typing import Final, final


@final
class WriteConcernDefaults:
    W: Final[int | str | None] = None
    JOURNAL: Final[bool] = False
    FSYNC: Final[bool] = False


@final
class WriteConcernKeys:
    W: Final[str] = "w"
    JOURNAL: Final[str] = "journal"
    FSYNC: Final[str] = "fsync"
