from collections.abc import Callable
from typing import Any

import pytest

from src.infrastructure.database.mongo.settings.constants import (
    WriteConcernDefaults as D,
)
from src.infrastructure.database.mongo.settings.constants import (
    WriteConcernKeys as K,
)
from src.infrastructure.database.mongo.settings.write_concern import (
    WriteConcernSettings,
)


@pytest.fixture(name="default_write_concern_settings")
def default() -> WriteConcernSettings:
    return WriteConcernSettings()


@pytest.fixture(name="custom_write_concern_settings")
def custom() -> Callable[[dict[str, Any]], WriteConcernSettings]:
    def _custom(**kwargs: Any) -> WriteConcernSettings:
        return WriteConcernSettings(**kwargs)

    return _custom


@pytest.fixture(name="default_write_concern_client_kwargs")
def default_client_kwargs() -> dict[str, Any]:
    return {K.JOURNAL: D.JOURNAL, K.FSYNC: D.FSYNC}
