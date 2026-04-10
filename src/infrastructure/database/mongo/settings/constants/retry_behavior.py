from typing import Final, final


@final
class RetryBehaviorDefaults:
    WRITES: Final[bool] = True
    READS: Final[bool] = True


@final
class RetryBehaviorKeys:
    WRITES: Final[str] = "retryWrites"
    READS: Final[str] = "retryReads"
