from collections.abc import Callable
from typing import Any

import pytest

from libs.mongo.constants.settings import (
    PoolDefaults as D,
)
from libs.mongo.constants.settings import (
    PoolKeys as K,
)
from libs.mongo.settings.pool import (
    PoolSettings,
)


@pytest.fixture(name="default_pool_settings")
def default() -> PoolSettings:
    return PoolSettings()


@pytest.fixture(name="custom_pool_settings")
def custom() -> Callable[[dict[str, Any]], PoolSettings]:
    def _custom(**kwargs: Any) -> PoolSettings:
        return PoolSettings(**kwargs)

    return _custom


@pytest.fixture(name="default_pool_client_kwargs")
def default_client_kwargs() -> dict[str, Any]:
    return {
        K.HEARTBEAT_FREQUENCY: D.HEARTBEAT_FREQUENCY,
        K.MAX_SIZE: D.MAX_SIZE,
        K.MIN_SIZE: D.MIN_SIZE,
        K.SERVER_MONITORING_MODE: D.SERVER_MONITORING_MODE,
    }
