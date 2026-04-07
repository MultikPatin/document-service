from typing import Any

import pytest
from pydantic import ValidationError

from src.infrastructure.database.mongo.settings.connection_mode import (
    ConnectionModeSettings,
)


def test_connection_mode_settings_valid_minimal() -> None:
    """Test valid minimal connection mode settings with default values."""
    settings = ConnectionModeSettings()
    assert settings.DIRECT_CONNECTION is None
    assert settings.APPNAME is None
    assert settings.READ_PREFERENCE is None
    assert settings.READ_PREFERENCE_TAGS is None
    assert settings.MAX_STALENESS_SECONDS is None
    assert settings.REPLICA_SET_NAME is None
    assert settings.client_kwargs == {}


def test_connection_mode_settings_valid_direct_connection() -> None:
    """Test valid DIRECT_CONNECTION field with True and False values."""
    # Test with True
    settings = ConnectionModeSettings(DIRECT_CONNECTION=True)
    assert settings.DIRECT_CONNECTION is True
    assert settings.client_kwargs == {"directConnection": True}

    # Test with False
    settings = ConnectionModeSettings(DIRECT_CONNECTION=False)
    assert settings.DIRECT_CONNECTION is False
    assert settings.client_kwargs == {"directConnection": False}

    # Test with None (default)
    settings = ConnectionModeSettings(DIRECT_CONNECTION=None)
    assert settings.DIRECT_CONNECTION is None
    assert settings.client_kwargs == {}


def test_connection_mode_settings_valid_appname() -> None:
    """Test valid APPNAME field with various string lengths."""
    # Test minimum length (1 character)
    appname = "a"
    settings = ConnectionModeSettings(APPNAME=appname)
    assert appname == settings.APPNAME
    assert settings.client_kwargs == {"appname": appname}

    # Test maximum length (128 characters)
    appname = "a" * 128
    settings = ConnectionModeSettings(APPNAME=appname)
    assert appname == settings.APPNAME
    assert settings.client_kwargs == {"appname": appname}


def test_connection_mode_settings_invalid_appname_too_long() -> None:
    """Test APPNAME field with 129 characters (invalid)."""
    appname = "a" * 129
    with pytest.raises(ValidationError):
        ConnectionModeSettings(APPNAME=appname)


def test_connection_mode_settings_valid_read_preference_primary() -> None:
    """Test valid READ_PREFERENCE field with 'primary'."""
    preference = "primary"
    settings = ConnectionModeSettings(READ_PREFERENCE=preference)
    assert preference == settings.READ_PREFERENCE
    assert settings.client_kwargs == {"readPreference": preference}


def test_connection_mode_settings_valid_read_preference_primary_preferred() -> (
    None
):
    """Test valid READ_PREFERENCE field with 'primaryPreferred'."""
    preference = "primaryPreferred"
    settings = ConnectionModeSettings(READ_PREFERENCE=preference)
    assert preference == settings.READ_PREFERENCE
    assert settings.client_kwargs == {"readPreference": preference}


def test_connection_mode_settings_valid_read_preference_secondary() -> None:
    """Test valid READ_PREFERENCE field with 'secondary'."""
    preference = "secondary"
    settings = ConnectionModeSettings(READ_PREFERENCE=preference)
    assert preference == settings.READ_PREFERENCE
    assert settings.client_kwargs == {"readPreference": preference}


def test_connection_mode_settings_valid_read_preference_secondary_preferred() -> (
    None
):
    """Test valid READ_PREFERENCE field with 'secondaryPreferred'."""
    preference = "secondaryPreferred"
    settings = ConnectionModeSettings(READ_PREFERENCE=preference)
    assert preference == settings.READ_PREFERENCE
    assert settings.client_kwargs == {"readPreference": preference}


def test_connection_mode_settings_valid_read_preference_nearest() -> None:
    """Test valid READ_PREFERENCE field with 'nearest'."""
    preference = "nearest"
    settings = ConnectionModeSettings(READ_PREFERENCE=preference)
    assert preference == settings.READ_PREFERENCE
    assert settings.client_kwargs == {"readPreference": preference}


def test_connection_mode_settings_invalid_read_preference() -> None:
    """Test READ_PREFERENCE field with invalid value."""
    # Test with None (default)
    settings = ConnectionModeSettings()
    assert settings.READ_PREFERENCE is None
    assert settings.client_kwargs == {}

    # Test with invalid values
    invalid_values = ["invalid", "master", "slave", "", "primary-preferred"]

    for value in invalid_values:
        with pytest.raises(ValidationError):
            ConnectionModeSettings(READ_PREFERENCE=value)


def test_connection_mode_settings_valid_read_preference_tags() -> None:
    """Test valid READ_PREFERENCE_TAGS field with various formats."""
    # Test simple key-value pair
    tags = "dc:ny"
    settings = ConnectionModeSettings(READ_PREFERENCE_TAGS=tags)
    assert tags == settings.READ_PREFERENCE_TAGS
    assert settings.client_kwargs == {"readPreferenceTags": tags}

    # Test multiple tags
    tags = "dc:ny,region:us-east"
    settings = ConnectionModeSettings(READ_PREFERENCE_TAGS=tags)
    assert tags == settings.READ_PREFERENCE_TAGS
    assert settings.client_kwargs == {"readPreferenceTags": tags}

    # Test empty string (allowed)
    tags = ""
    settings = ConnectionModeSettings(READ_PREFERENCE_TAGS=tags)
    assert tags == settings.READ_PREFERENCE_TAGS
    assert settings.client_kwargs == {"readPreferenceTags": tags}

    # Test with None (default)
    settings = ConnectionModeSettings(READ_PREFERENCE_TAGS=None)
    assert settings.READ_PREFERENCE_TAGS is None
    assert settings.client_kwargs == {}


def test_connection_mode_settings_valid_max_staleness_seconds() -> None:
    """Test valid MAX_STALENESS_SECONDS field with various values."""
    # Test zero (minimum value)
    seconds = 0
    settings = ConnectionModeSettings(MAX_STALENESS_SECONDS=seconds)
    assert seconds == settings.MAX_STALENESS_SECONDS
    assert settings.client_kwargs == {"maxStalenessSeconds": seconds}

    # Test positive value
    seconds = 1000
    settings = ConnectionModeSettings(MAX_STALENESS_SECONDS=seconds)
    assert seconds == settings.MAX_STALENESS_SECONDS
    assert settings.client_kwargs == {"maxStalenessSeconds": seconds}

    # Test maximum value (90000)
    seconds = 90000
    settings = ConnectionModeSettings(MAX_STALENESS_SECONDS=seconds)
    assert seconds == settings.MAX_STALENESS_SECONDS
    assert settings.client_kwargs == {"maxStalenessSeconds": seconds}

    # Test with None (default)
    settings = ConnectionModeSettings(MAX_STALENESS_SECONDS=None)
    assert settings.MAX_STALENESS_SECONDS is None
    assert settings.client_kwargs == {}


def test_connection_mode_settings_invalid_max_staleness_seconds_negative() -> (
    None
):
    """Test MAX_STALENESS_SECONDS field with negative value (invalid)."""
    with pytest.raises(ValidationError):
        ConnectionModeSettings(MAX_STALENESS_SECONDS=-1)


def test_connection_mode_settings_invalid_max_staleness_seconds_too_high() -> (
    None
):
    """Test MAX_STALENESS_SECONDS field with value greater than 90000 (invalid)."""
    with pytest.raises(ValidationError):
        ConnectionModeSettings(MAX_STALENESS_SECONDS=90001)


def test_connection_mode_settings_invalid_max_staleness_seconds_non_integer() -> (
    None
):
    """Test MAX_STALENESS_SECONDS field with non-integer value (invalid)."""
    # Test with string (invalid)
    with pytest.raises(ValidationError):
        ConnectionModeSettings(MAX_STALENESS_SECONDS="invalid")

    # Test with float string (invalid)
    with pytest.raises(ValidationError):
        ConnectionModeSettings(MAX_STALENESS_SECONDS="3.5")

    # Test with empty string (invalid)
    with pytest.raises(ValidationError):
        ConnectionModeSettings(MAX_STALENESS_SECONDS="")

    # Test with float (invalid)
    with pytest.raises(ValidationError):
        ConnectionModeSettings(MAX_STALENESS_SECONDS=3.5)

    # Test with negative integer (invalid)
    with pytest.raises(ValidationError):
        ConnectionModeSettings(MAX_STALENESS_SECONDS=-1)

    # Test with too high integer (invalid)
    with pytest.raises(ValidationError):
        ConnectionModeSettings(MAX_STALENESS_SECONDS=90001)

    # Test with valid integer (should pass)
    valid_seconds = 45000
    settings = ConnectionModeSettings(MAX_STALENESS_SECONDS=valid_seconds)
    assert valid_seconds == settings.MAX_STALENESS_SECONDS
    assert {"maxStalenessSeconds": valid_seconds} == settings.client_kwargs


def test_connection_mode_settings_valid_replica_set_name() -> None:
    """Test valid REPLICA_SET_NAME field with various string lengths."""
    # Test minimum length (1 character)
    name = "a"
    settings = ConnectionModeSettings(REPLICA_SET_NAME=name)
    assert name == settings.REPLICA_SET_NAME
    assert settings.client_kwargs == {"replicaSet": name}

    # Test maximum length (128 characters)
    name = "a" * 128
    settings = ConnectionModeSettings(REPLICA_SET_NAME=name)
    assert name == settings.REPLICA_SET_NAME
    assert settings.client_kwargs == {"replicaSet": name}


def test_connection_mode_settings_invalid_replica_set_name_empty() -> None:
    """Test REPLICA_SET_NAME field with empty string (invalid)."""
    with pytest.raises(ValidationError):
        ConnectionModeSettings(REPLICA_SET_NAME="")


def test_connection_mode_settings_invalid_replica_set_name_too_long() -> None:
    """Test REPLICA_SET_NAME field with 129 characters (invalid)."""
    name = "a" * 129
    with pytest.raises(ValidationError):
        ConnectionModeSettings(REPLICA_SET_NAME=name)


def test_connection_mode_settings_client_kwargs_empty() -> None:
    """Test client_kwargs returns empty dict when no values set."""
    settings = ConnectionModeSettings()
    assert settings.client_kwargs == {}


def test_connection_mode_settings_client_kwargs_all_fields() -> None:
    """Test client_kwargs returns correct dictionary when all fields are set."""
    settings = ConnectionModeSettings(
        DIRECT_CONNECTION=True,
        APPNAME="myapp",
        READ_PREFERENCE="secondary",
        READ_PREFERENCE_TAGS="dc:ny,region:us-east",
        MAX_STALENESS_SECONDS=3600,
        REPLICA_SET_NAME="rs0",
    )
    expected_kwargs: dict[str, Any] = {
        "directConnection": True,
        "appname": "myapp",
        "readPreference": "secondary",
        "readPreferenceTags": "dc:ny,region:us-east",
        "maxStalenessSeconds": 3600,
        "replicaSet": "rs0",
    }
    assert settings.client_kwargs == expected_kwargs


def test_connection_mode_settings_client_kwargs_partial_fields() -> None:
    """Test client_kwargs returns correct dictionary with partial fields set."""
    # Test with only APPNAME and MAX_STALENESS_SECONDS
    settings = ConnectionModeSettings(
        APPNAME="myapp", MAX_STALENESS_SECONDS=1800
    )
    expected_kwargs: dict[str, Any] = {
        "appname": "myapp",
        "maxStalenessSeconds": 1800,
    }
    assert settings.client_kwargs == expected_kwargs

    # Test with only READ_PREFERENCE and READ_PREFERENCE_TAGS
    settings = ConnectionModeSettings(
        READ_PREFERENCE="secondaryPreferred",
        READ_PREFERENCE_TAGS="dc:ny",
    )
    expected_kwargs = {
        "readPreference": "secondaryPreferred",
        "readPreferenceTags": "dc:ny",
    }
    assert settings.client_kwargs == expected_kwargs


def test_connection_mode_settings_client_kwargs_none_values() -> None:
    """Test client_kwargs excludes keys when values are None or empty string."""
    # Test with None values (explicit)
    settings = ConnectionModeSettings(
        DIRECT_CONNECTION=None,
        APPNAME=None,
        READ_PREFERENCE=None,
        READ_PREFERENCE_TAGS=None,
        MAX_STALENESS_SECONDS=None,
        REPLICA_SET_NAME=None,
    )
    assert settings.client_kwargs == {}

    # Test with empty string for READ_PREFERENCE_TAGS (should be included)
    settings = ConnectionModeSettings(READ_PREFERENCE_TAGS="")
    assert settings.client_kwargs == {"readPreferenceTags": ""}

    # Test with empty string for other string fields (should be excluded)
    settings = ConnectionModeSettings(APPNAME="")
    assert settings.client_kwargs == {}

    # Test with empty string for READ_PREFERENCE_TAGS (should be included)
    settings = ConnectionModeSettings(READ_PREFERENCE_TAGS="")
    assert settings.client_kwargs == {"readPreferenceTags": ""}

    # Test with None for all fields
    settings = ConnectionModeSettings(
        DIRECT_CONNECTION=None,
        APPNAME=None,
        READ_PREFERENCE=None,
        READ_PREFERENCE_TAGS=None,
        MAX_STALENESS_SECONDS=None,
        REPLICA_SET_NAME=None,
    )
    assert settings.client_kwargs == {}

    # Test with empty string for APPNAME (should be excluded)
    settings = ConnectionModeSettings(APPNAME="")
    assert settings.client_kwargs == {}
