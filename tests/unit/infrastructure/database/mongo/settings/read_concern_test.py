from typing import Any

import pytest
from pydantic import ValidationError

from src.infrastructure.database.mongo.settings.constants import (
    ReadConcernDefaults,
)
from src.infrastructure.database.mongo.settings.read_concern import (
    ReadConcernSettings,
)


def test_read_concern_settings_default_level() -> None:
    """Test that ReadConcernSettings uses default level from constants."""
    settings = ReadConcernSettings()
    assert settings.LEVEL == ReadConcernDefaults.LEVEL


@pytest.mark.parametrize(
    "level",
    ["local", "majority", "linearizable"],
    ids=["local", "majority", "linearizable"],
)
def test_read_concern_settings_valid_levels(level) -> None:
    """Test that ReadConcernSettings accepts all valid read concern levels."""
    settings = ReadConcernSettings(LEVEL=level)
    assert level == settings.LEVEL


@pytest.mark.parametrize(
    ("level", "expected_level"),
    [
        ("linearizable", "linearizable"),
        (ReadConcernDefaults.LEVEL, ReadConcernDefaults.LEVEL),
    ],
    ids=["linear", "random"],
)
def test_read_concern_settings_client_kwargs(level, expected_level) -> None:
    """Test that client_kwargs property returns correct dictionary with read concern level."""
    settings = ReadConcernSettings(LEVEL=level)
    expected: dict[str, Any] = {"readConcernLevel": expected_level}
    assert settings.client_kwargs == expected


@pytest.mark.parametrize(
    "level",
    ["invalid", "", "unknown", "123", "LOCAL", "available", "snapshot"],
    ids=[
        "invalid",
        "empty",
        "unknown",
        "number",
        "local",
        "available",
        "snapshot",
    ],
)
def test_read_concern_settings_invalid_level(level) -> None:
    """Test that ReadConcernSettings rejects invalid read concern levels."""
    with pytest.raises(ValidationError):
        ReadConcernSettings(LEVEL=level)
