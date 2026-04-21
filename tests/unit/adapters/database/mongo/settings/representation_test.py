from typing import Any

import pytest
from pydantic import ValidationError

from libs.mongo.constants.settings import (
    RepresentationDefaults as D,
)
from libs.mongo.settings.representation import (
    RepresentationSettings,
)


def test_representation_settings_default(
    default_representation_settings, default_representation_client_kwargs
) -> None:
    """Test default values for RepresentationSettings."""
    s = default_representation_settings

    assert s.UUID == D.UUID
    assert s.client_kwargs == default_representation_client_kwargs


def test_representation_settings_default_values() -> None:
    """Test that RepresentationSettings uses default values from RepresentationDefaults when no values are provided."""
    settings = RepresentationSettings()

    assert settings.UUID == D.UUID


@pytest.mark.parametrize(
    "uuid_format",
    [
        "standard",
        "pythonLegacy",
        "javaLegacy",
        "csharpLegacy",
        "unspecified",
    ],
    ids=[
        "standard",
        "pythonLegacy",
        "javaLegacy",
        "csharpLegacy",
        "unspecified",
    ],
)
def test_representation_settings_valid_values(uuid_format: str) -> None:
    """Test that RepresentationSettings accepts valid values for UUID field."""
    settings = RepresentationSettings(UUID=uuid_format)
    assert uuid_format == settings.UUID


@pytest.mark.parametrize(
    "uuid_format",
    [
        "invalid",
        "",
        "Standard",
        "python-legacy",
        "random",
    ],
    ids=[
        "invalid",
        "empty",
        "Case sensitive",
        "Wrong format",
        "Not in allowed values",
    ],
)
def test_representation_settings_invalid_values(uuid_format: str) -> None:
    """Test that RepresentationSettings raises ValidationError for invalid UUID values."""
    with pytest.raises(ValidationError):
        RepresentationSettings(UUID=uuid_format)


@pytest.mark.parametrize(
    ("uuid_format", "expected_value"),
    [
        (None, D.UUID),
        ("standard", "standard"),
        ("pythonLegacy", "pythonLegacy"),
        ("javaLegacy", "javaLegacy"),
        ("csharpLegacy", "csharpLegacy"),
        ("unspecified", "unspecified"),
    ],
)
def test_representation_settings_client_kwargs(
    uuid_format: str | None,
    expected_value: str,
    default_representation_client_kwargs: dict[str, Any],
) -> None:
    """Test client_kwargs returns correct dictionary for different UUID representations."""
    # Arrange
    if uuid_format is None:
        settings = RepresentationSettings()
    else:
        settings = RepresentationSettings(UUID=uuid_format)

    default_representation_client_kwargs["uuidRepresentation"] = expected_value

    # Act & Assert
    assert settings.client_kwargs == default_representation_client_kwargs
