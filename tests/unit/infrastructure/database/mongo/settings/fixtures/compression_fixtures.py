from typing import Any

import pytest

from src.infrastructure.database.mongo.settings.compression import (
    CompressionSettings,
)


@pytest.fixture(name="default_compression_settings")
def default() -> CompressionSettings:
    return CompressionSettings()


@pytest.fixture(name="default_compression_client_kwargs")
def default_client_kwargs() -> dict[str, Any]:
    return {}
