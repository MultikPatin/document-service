from typing import Any

import pytest
from libs.mongo.constants.settings import (
    ReadConcernDefaults as D,
)
from libs.mongo.settings.read_concern import (
    ReadConcernSettings,
)
from pydantic import ValidationError


def test_read_concern_settings_default(
    default_read_concern_settings, default_read_concern_client_kwargs
) -> None:
    """Test default values for ReadConcernSettings."""
    s = default_read_concern_settings

    assert s.LEVEL == D.LEVEL
    assert s.client_kwargs == default_read_concern_client_kwargs


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
        (D.LEVEL, D.LEVEL),
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
