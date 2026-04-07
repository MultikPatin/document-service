from typing import Any

import pytest
from pydantic import ValidationError

from src.infrastructure.database.mongo.settings.constants import (
    RepresentationDefaults,
)
from src.infrastructure.database.mongo.settings.representation import (
    RepresentationSettings,
)


def test_representation_settings_default_values() -> None:
    """Test that RepresentationSettings uses default values from RepresentationDefaults when no values are provided."""
    settings = RepresentationSettings()

    assert settings.UUID == RepresentationDefaults.UUID


def test_representation_settings_valid_values() -> None:
    """Test that RepresentationSettings accepts valid values for UUID field."""
    # Test all valid UUID representation formats
    valid_uuid_formats = [
        "standard",
        "pythonLegacy",
        "javaLegacy",
        "csharpLegacy",
        "unspecified",
    ]

    for uuid_format in valid_uuid_formats:
        settings = RepresentationSettings(UUID=uuid_format)
        assert uuid_format == settings.UUID


def test_representation_settings_invalid_values() -> None:
    """Test that RepresentationSettings raises ValidationError for invalid UUID values."""
    # Test invalid UUID representation formats
    invalid_uuid_formats = [
        "invalid",
        "",
        "Standard",  # Case sensitive
        "python-legacy",  # Wrong format
        "random",  # Not in allowed values
    ]

    for uuid_format in invalid_uuid_formats:
        with pytest.raises(ValidationError):
            RepresentationSettings(UUID=uuid_format)


def test_representation_settings_client_kwargs_with_default() -> None:
    """Test client_kwargs returns correct dictionary with default UUID representation."""
    settings = RepresentationSettings()
    expected: dict[str, Any] = {
        "uuidRepresentation": RepresentationDefaults.UUID
    }
    assert settings.client_kwargs == expected


def test_representation_settings_client_kwargs_with_standard() -> None:
    """Test client_kwargs returns correct dictionary with standard UUID representation."""
    settings = RepresentationSettings(UUID="standard")
    expected: dict[str, Any] = {"uuidRepresentation": "standard"}
    assert settings.client_kwargs == expected


def test_representation_settings_client_kwargs_with_python_legacy() -> None:
    """Test client_kwargs returns correct dictionary with pythonLegacy UUID representation."""
    settings = RepresentationSettings(UUID="pythonLegacy")
    expected: dict[str, Any] = {"uuidRepresentation": "pythonLegacy"}
    assert settings.client_kwargs == expected


def test_representation_settings_client_kwargs_with_java_legacy() -> None:
    """Test client_kwargs returns correct dictionary with javaLegacy UUID representation."""
    settings = RepresentationSettings(UUID="javaLegacy")
    expected: dict[str, Any] = {"uuidRepresentation": "javaLegacy"}
    assert settings.client_kwargs == expected


def test_representation_settings_client_kwargs_with_csharp_legacy() -> None:
    """Test client_kwargs returns correct dictionary with csharpLegacy UUID representation."""
    settings = RepresentationSettings(UUID="csharpLegacy")
    expected: dict[str, Any] = {"uuidRepresentation": "csharpLegacy"}
    assert settings.client_kwargs == expected


def test_representation_settings_client_kwargs_with_unspecified() -> None:
    """Test client_kwargs returns correct dictionary with unspecified UUID representation."""
    settings = RepresentationSettings(UUID="unspecified")
    expected: dict[str, Any] = {"uuidRepresentation": "unspecified"}
    assert settings.client_kwargs == expected
