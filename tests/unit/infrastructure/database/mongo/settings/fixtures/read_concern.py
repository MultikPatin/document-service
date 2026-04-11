from collections.abc import Callable
from typing import Any

import pytest

from src.infrastructure.database.mongo.settings.constants import (
    ReadConcernDefaults as D,
)
from src.infrastructure.database.mongo.settings.constants import (
    ReadConcernKeys as K,
)
from src.infrastructure.database.mongo.settings.read_concern import (
    ReadConcernSettings,
)


@pytest.fixture(name="default_read_concern_settings")
def default() -> ReadConcernSettings:
    return ReadConcernSettings()


@pytest.fixture(name="custom_read_concern_settings")
def custom() -> Callable[[dict[str, Any]], ReadConcernSettings]:
    def _custom(**kwargs: Any) -> ReadConcernSettings:
        return ReadConcernSettings(**kwargs)

    return _custom


@pytest.fixture(name="default_read_concern_client_kwargs")
def default_client_kwargs() -> dict[str, Any]:
    return {K.LEVEL: D.LEVEL}
