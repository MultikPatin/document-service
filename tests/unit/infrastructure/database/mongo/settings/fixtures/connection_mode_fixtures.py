from typing import Any

import pytest

from src.infrastructure.database.mongo.settings.connection_mode import (
    ConnectionModeSettings,
)


@pytest.fixture(name="default_connection_mode_settings")
def default() -> ConnectionModeSettings:
    return ConnectionModeSettings()


@pytest.fixture(name="default_connection_mode_client_kwargs")
def default_client_kwargs() -> dict[str, Any]:
    return {}
