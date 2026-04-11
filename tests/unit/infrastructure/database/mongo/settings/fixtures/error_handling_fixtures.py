from collections.abc import Callable
from typing import Any

import pytest

from src.infrastructure.database.mongo.settings.constants import (
    ErrorHandlingDefaults as D,
)
from src.infrastructure.database.mongo.settings.constants import (
    ErrorHandlingKeys as K,
)
from src.infrastructure.database.mongo.settings.erro_handling import (
    ErrorHandlingSettings,
)


@pytest.fixture(name="default_erro_handling_settings")
def default() -> ErrorHandlingSettings:
    return ErrorHandlingSettings()


@pytest.fixture(name="custom_erro_handling_settings")
def custom() -> Callable[[dict[str, Any]], ErrorHandlingSettings]:
    def _custom(**kwargs: Any) -> ErrorHandlingSettings:
        return ErrorHandlingSettings(**kwargs)

    return _custom


@pytest.fixture(name="default_erro_handling_client_kwargs")
def default_client_kwargs() -> dict[str, Any]:
    return {K.UNICODE_DECODE: D.UNICODE_DECODE}
