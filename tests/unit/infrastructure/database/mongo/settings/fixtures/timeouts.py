from collections.abc import Callable
from typing import Any

import pytest

from src.infrastructure.database.mongo.settings.constants import (
    TimeoutsDefaults as D,
)
from src.infrastructure.database.mongo.settings.constants import (
    TimeoutsKeys as K,
)
from src.infrastructure.database.mongo.settings.timeouts import (
    TimeoutsSettings,
)


@pytest.fixture(name="default_timeouts_settings")
def default() -> TimeoutsSettings:
    return TimeoutsSettings()


@pytest.fixture(name="custom_timeouts_settings")
def custom() -> Callable[[dict[str, Any]], TimeoutsSettings]:
    def _custom(**kwargs: Any) -> TimeoutsSettings:
        return TimeoutsSettings(**kwargs)

    return _custom


@pytest.fixture(name="default_timeouts_client_kwargs")
def default_client_kwargs() -> dict[str, Any]:
    return {
        K.CONNECTION: D.CONNECTION,
        K.SOCKET: D.SOCKET,
        K.SERVER_SELECTION: D.SERVER_SELECTION,
    }
