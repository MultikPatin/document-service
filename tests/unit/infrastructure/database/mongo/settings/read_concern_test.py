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


def test_read_concern_settings_valid_levels() -> None:
    """Test that ReadConcernSettings accepts all valid read concern levels."""
    valid_levels = ["local", "majority", "linearizable"]

    for level in valid_levels:
        settings = ReadConcernSettings(LEVEL=level)
        assert level == settings.LEVEL


def test_read_concern_settings_invalid_level() -> None:
    """Test that ReadConcernSettings rejects invalid read concern levels."""
    invalid_levels = ["invalid", "", "unknown", "123", "LOCAL"]

    for level in invalid_levels:
        with pytest.raises(ValidationError):
            ReadConcernSettings(LEVEL=level)


def test_read_concern_settings_client_kwargs() -> None:
    """Test that client_kwargs property returns correct dictionary with read concern level."""
    level = "linearizable"
    settings = ReadConcernSettings(LEVEL=level)
    expected: dict[str, Any] = {"readConcernLevel": level}
    assert settings.client_kwargs == expected


def test_read_concern_settings_client_kwargs_with_default() -> None:
    """Test that client_kwargs property returns correct dictionary with default level."""
    settings = ReadConcernSettings()
    expected: dict[str, Any] = {"readConcernLevel": ReadConcernDefaults.LEVEL}
    assert settings.client_kwargs == expected
