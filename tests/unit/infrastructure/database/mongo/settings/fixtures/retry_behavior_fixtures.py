from collections.abc import Callable
from typing import Any

import pytest

from src.infrastructure.database.mongo.settings.constants import (
    RetryBehaviorDefaults as D,
)
from src.infrastructure.database.mongo.settings.constants import (
    RetryBehaviorKeys as K,
)
from src.infrastructure.database.mongo.settings.retry_behavior import (
    RetryBehaviorSettings,
)


@pytest.fixture(name="default_retry_behavior_settings")
def default() -> RetryBehaviorSettings:
    return RetryBehaviorSettings()


@pytest.fixture(name="custom_retry_behavior_settings")
def custom() -> Callable[[dict[str, Any]], RetryBehaviorSettings]:
    def _custom(**kwargs: Any) -> RetryBehaviorSettings:
        return RetryBehaviorSettings(**kwargs)

    return _custom


@pytest.fixture(name="default_retry_behavior_client_kwargs")
def default_client_kwargs() -> dict[str, Any]:
    return {K.WRITES: D.WRITES, K.READS: D.READS}
