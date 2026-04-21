from collections.abc import Callable
from typing import Any

import pytest

from libs.mongo.settings import (
    ConnectionModeSettings,
)


@pytest.fixture(name="default_connection_mode_settings")
def default() -> ConnectionModeSettings:
    return ConnectionModeSettings()


@pytest.fixture(name="custom_connection_mode_settings")
def custom() -> Callable[[dict[str, Any]], ConnectionModeSettings]:
    def _custom(**kwargs: Any) -> ConnectionModeSettings:
        return ConnectionModeSettings(**kwargs)

    return _custom


@pytest.fixture(name="default_connection_mode_client_kwargs")
def default_client_kwargs() -> dict[str, Any]:
    return {}
