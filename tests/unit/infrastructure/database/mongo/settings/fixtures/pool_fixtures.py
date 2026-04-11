from collections.abc import Callable
from typing import Any

import pytest

from src.infrastructure.database.mongo.settings.pool import (
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
    return {}
