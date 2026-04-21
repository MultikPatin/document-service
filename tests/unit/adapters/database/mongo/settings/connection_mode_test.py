from typing import Any

import pytest
from pydantic import ValidationError

from libs.mongo.constants.settings import (
    ConnectionModeDefaults as Defaults,
)
from libs.mongo.settings import (
    ConnectionModeSettings,
)


def test_connection_mode_settings_default(
    default_connection_mode_settings, default_connection_mode_client_kwargs
) -> None:
    """Test default values for ConnectionModeSettings."""
    s = default_connection_mode_settings
    assert s.DIRECT_CONNECTION == Defaults.DIRECT_CONNECTION
    assert s.APPNAME == Defaults.APPNAME
    assert s.READ_PREFERENCE == Defaults.READ_PREFERENCE
    assert s.READ_PREFERENCE_TAGS == Defaults.READ_PREFERENCE_TAGS
    assert s.MAX_STALENESS_SECONDS == Defaults.MAX_STALENESS_SECONDS
    assert s.REPLICA_SET_NAME == Defaults.REPLICA_SET_NAME
    assert s.client_kwargs == default_connection_mode_client_kwargs


@pytest.mark.parametrize(
    ("direct_connection_value", "expected_client_kwarg"),
    [
        (True, {"directConnection": True}),
        (False, {"directConnection": False}),
        (None, {}),
    ],
    ids=["true", "false", "none"],
)
def test_connection_mode_settings_valid_direct_connection(
    direct_connection_value: bool | None,
    expected_client_kwarg: dict[str, Any],
) -> None:
    """Test valid DIRECT_CONNECTION field with various values."""
    settings = ConnectionModeSettings(DIRECT_CONNECTION=direct_connection_value)
    assert direct_connection_value == settings.DIRECT_CONNECTION
    assert settings.client_kwargs == expected_client_kwarg


@pytest.mark.parametrize(
    "appname_length",
    [1, 128],
    ids=["min-length", "max-length"],
)
def test_connection_mode_settings_valid_appname(
    appname_length: int,
) -> None:
    """Test valid APPNAME field with various string lengths."""
    appname = "a" * appname_length
    settings = ConnectionModeSettings(APPNAME=appname)
    assert appname == settings.APPNAME
    assert settings.client_kwargs == {"appname": appname}


@pytest.mark.parametrize(
    "read_preference",
    [
        "primary",
        "primaryPreferred",
        "secondary",
        "secondaryPreferred",
        "nearest",
    ],
    ids=[
        "primary",
        "primary-preferred",
        "secondary",
        "secondary-preferred",
        "nearest",
    ],
)
def test_connection_mode_settings_valid_read_preference(
    read_preference: str,
) -> None:
    """Test valid READ_PREFERENCE field with various values."""
    settings = ConnectionModeSettings(READ_PREFERENCE=read_preference)
    assert read_preference == settings.READ_PREFERENCE
    assert settings.client_kwargs == {"readPreference": read_preference}


@pytest.mark.parametrize(
    ("tags", "kwargs"),
    [
        ("dc:ny", {"readPreferenceTags": "dc:ny"}),
        (
            "dc:ny,region:us-east",
            {"readPreferenceTags": "dc:ny,region:us-east"},
        ),
        ("", {"readPreferenceTags": ""}),
        (None, {}),
    ],
)
def test_connection_mode_settings_valid_read_preference_tags(
    tags, kwargs
) -> None:
    """Test valid READ_PREFERENCE_TAGS field with various formats."""
    settings = ConnectionModeSettings(READ_PREFERENCE_TAGS=tags)
    assert tags == settings.READ_PREFERENCE_TAGS
    assert settings.client_kwargs == kwargs


@pytest.mark.parametrize(
    "max_staleness_seconds",
    [0, 1000, 90000],
    ids=["min-value", "mid-value", "max-value"],
)
def test_connection_mode_settings_valid_max_staleness_seconds(
    max_staleness_seconds: int,
) -> None:
    """Test valid MAX_STALENESS_SECONDS field with various values."""
    settings = ConnectionModeSettings(
        MAX_STALENESS_SECONDS=max_staleness_seconds
    )
    assert max_staleness_seconds == settings.MAX_STALENESS_SECONDS
    assert settings.client_kwargs == {
        "maxStalenessSeconds": max_staleness_seconds
    }


@pytest.mark.parametrize(
    "replica_set_name_length",
    [1, 128],
    ids=["min-length", "max-length"],
)
def test_connection_mode_settings_valid_replica_set_name(
    replica_set_name_length: int,
) -> None:
    """Test valid REPLICA_SET_NAME field with various string lengths."""
    name = "a" * replica_set_name_length
    settings = ConnectionModeSettings(REPLICA_SET_NAME=name)
    assert name == settings.REPLICA_SET_NAME
    assert settings.client_kwargs == {"replicaSet": name}


@pytest.mark.parametrize(
    ("field_values", "expected_kwargs"),
    [
        (
            {},
            {},
        ),
        (
            {
                "DIRECT_CONNECTION": True,
                "APPNAME": "myapp",
                "READ_PREFERENCE": "secondary",
                "READ_PREFERENCE_TAGS": "dc:ny,region:us-east",
                "MAX_STALENESS_SECONDS": 3600,
                "REPLICA_SET_NAME": "rs0",
            },
            {
                "directConnection": True,
                "appname": "myapp",
                "readPreference": "secondary",
                "readPreferenceTags": "dc:ny,region:us-east",
                "maxStalenessSeconds": 3600,
                "replicaSet": "rs0",
            },
        ),
        (
            {"APPNAME": "myapp", "MAX_STALENESS_SECONDS": 1800},
            {"appname": "myapp", "maxStalenessSeconds": 1800},
        ),
        (
            {
                "READ_PREFERENCE": "secondaryPreferred",
                "READ_PREFERENCE_TAGS": "dc:ny",
            },
            {
                "readPreference": "secondaryPreferred",
                "readPreferenceTags": "dc:ny",
            },
        ),
        (
            {
                "DIRECT_CONNECTION": None,
                "APPNAME": None,
                "READ_PREFERENCE": None,
                "READ_PREFERENCE_TAGS": None,
                "MAX_STALENESS_SECONDS": None,
                "REPLICA_SET_NAME": None,
            },
            {},
        ),
        (
            {"READ_PREFERENCE_TAGS": ""},
            {"readPreferenceTags": ""},
        ),
    ],
)
def test_connection_mode_settings_client_kwargs(
    field_values: dict[str, Any],
    expected_kwargs: dict[str, Any],
) -> None:
    """Test client_kwargs returns correct dictionary for various field combinations."""
    settings = ConnectionModeSettings(**field_values)
    assert settings.client_kwargs == expected_kwargs


@pytest.mark.parametrize(
    "value",
    ["invalid", "master", "slave", "", "primary-preferred"],
)
def test_connection_mode_settings_invalid_read_preference(value) -> None:
    """Test READ_PREFERENCE field with invalid values."""
    # Test with None (default)
    with pytest.raises(ValidationError):
        ConnectionModeSettings(READ_PREFERENCE=value)


@pytest.mark.parametrize(
    "value",
    ["invalid", "3.5", "", 3.5, -1, 90001],
)
def test_connection_mode_settings_invalid_max_staleness_seconds(
    value,
) -> None:
    """Test MAX_STALENESS_SECONDS field with noninteger value (invalid)."""
    # Test with string (invalid)
    with pytest.raises(ValidationError):
        ConnectionModeSettings(MAX_STALENESS_SECONDS=value)


@pytest.mark.parametrize(
    "value",
    ["", "a" * 129],
)
def test_connection_mode_settings_invalid_replica_set_name(value) -> None:
    """Test REPLICA_SET_NAME field with empty string (invalid)."""
    with pytest.raises(ValidationError):
        ConnectionModeSettings(REPLICA_SET_NAME=value)


@pytest.mark.parametrize(
    "value",
    ["", "a" * 129],
)
def test_connection_mode_settings_invalid_appname(value) -> None:
    """Test APPNAME field with 129 characters (invalid)."""
    with pytest.raises(ValidationError):
        ConnectionModeSettings(APPNAME=value)
