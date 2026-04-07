from typing import Any

import pytest
from pydantic import ValidationError

from src.infrastructure.database.mongo.settings.constants import PoolDefaults
from src.infrastructure.database.mongo.settings.pool import PoolSettings


def test_pool_settings_default_values() -> None:
    """Test that PoolSettings uses default values from PoolDefaults when no values are provided."""
    settings = PoolSettings()

    assert settings.MAX_SIZE == PoolDefaults.MAX_SIZE
    assert settings.MIN_SIZE == PoolDefaults.MIN_SIZE
    assert settings.MAX_IDLE_TIME_MS == PoolDefaults.MAX_IDLE_TIME_MS
    assert settings.MAX_CONNECTING == PoolDefaults.MAX_CONNECTING
    assert settings.WAIT_QUEUE_TIMEOUT_MS == PoolDefaults.WAIT_QUEUE_TIMEOUT_MS
    assert (
        settings.HEARTBEAT_FREQUENCY_MS == PoolDefaults.HEARTBEAT_FREQUENCY_MS
    )
    assert (
        settings.SERVER_MONITORING_MODE == PoolDefaults.SERVER_MONITORING_MODE
    )


def test_pool_settings_valid_values() -> None:
    """Test that PoolSettings accepts valid values for all fields."""
    test_max_size = 500
    test_min_size = 10
    test_max_idle_time_ms = 30000
    test_max_connecting = 50
    test_wait_queue_timeout_ms = 15000
    test_heartbeat_frequency_ms = 5000
    server_monitoring_mode = "poll"

    settings = PoolSettings(
        MAX_SIZE=test_max_size,
        MIN_SIZE=test_min_size,
        MAX_IDLE_TIME_MS=test_max_idle_time_ms,
        MAX_CONNECTING=test_max_connecting,
        WAIT_QUEUE_TIMEOUT_MS=test_wait_queue_timeout_ms,
        HEARTBEAT_FREQUENCY_MS=test_heartbeat_frequency_ms,
        SERVER_MONITORING_MODE=server_monitoring_mode,
    )

    assert test_max_size == settings.MAX_SIZE
    assert test_min_size == settings.MIN_SIZE
    assert test_max_idle_time_ms == settings.MAX_IDLE_TIME_MS
    assert test_max_connecting == settings.MAX_CONNECTING
    assert test_wait_queue_timeout_ms == settings.WAIT_QUEUE_TIMEOUT_MS
    assert test_heartbeat_frequency_ms == settings.HEARTBEAT_FREQUENCY_MS
    assert server_monitoring_mode == settings.SERVER_MONITORING_MODE


def test_pool_settings_none_values() -> None:
    """Test that PoolSettings accepts None for all optional fields."""
    settings = PoolSettings(
        MAX_SIZE=None,
        MIN_SIZE=None,
        MAX_IDLE_TIME_MS=None,
        MAX_CONNECTING=None,
        WAIT_QUEUE_TIMEOUT_MS=None,
        HEARTBEAT_FREQUENCY_MS=None,
        SERVER_MONITORING_MODE=None,
    )

    assert settings.MAX_SIZE is None
    assert settings.MIN_SIZE is None
    assert settings.MAX_IDLE_TIME_MS is None
    assert settings.MAX_CONNECTING is None
    assert settings.WAIT_QUEUE_TIMEOUT_MS is None
    assert settings.HEARTBEAT_FREQUENCY_MS is None
    assert settings.SERVER_MONITORING_MODE is None


def test_pool_settings_max_size_validation() -> None:
    """Test MAX_SIZE validation with boundary and invalid values."""
    # Valid boundary values
    assert PoolSettings(MAX_SIZE=1).MAX_SIZE == 1
    assert (
        PoolSettings(MAX_SIZE=PoolDefaults.MAX_SIZE).MAX_SIZE
        == PoolDefaults.MAX_SIZE
    )

    # Invalid values
    with pytest.raises(ValidationError):
        PoolSettings(MAX_SIZE=0)
    with pytest.raises(ValidationError):
        PoolSettings(MAX_SIZE=1001)
    with pytest.raises(ValidationError):
        PoolSettings(MAX_SIZE=-1)


def test_pool_settings_min_size_validation() -> None:
    """Test MIN_SIZE validation with boundary and invalid values."""
    # Valid boundary values
    assert PoolSettings(MIN_SIZE=0).MIN_SIZE == 0
    assert (
        PoolSettings(MIN_SIZE=PoolDefaults.MIN_SIZE).MIN_SIZE
        == PoolDefaults.MIN_SIZE
    )

    # Invalid values
    with pytest.raises(ValidationError):
        PoolSettings(MIN_SIZE=-1)
    with pytest.raises(ValidationError):
        PoolSettings(MIN_SIZE=1000)


def test_pool_settings_max_connecting_validation() -> None:
    """Test MAX_CONNECTING validation with boundary and invalid values."""
    # Valid boundary values
    assert PoolSettings(MAX_CONNECTING=1).MAX_CONNECTING == 1
    assert (
        PoolSettings(MAX_CONNECTING=PoolDefaults.MAX_CONNECTING).MAX_CONNECTING
        == PoolDefaults.MAX_CONNECTING
    )

    # Invalid values
    with pytest.raises(ValidationError):
        PoolSettings(MAX_CONNECTING=0)
    with pytest.raises(ValidationError):
        PoolSettings(MAX_CONNECTING=101)
    with pytest.raises(ValidationError):
        PoolSettings(MAX_CONNECTING=-1)


def test_pool_settings_server_monitoring_mode_validation() -> None:
    """Test SERVER_MONITORING_MODE validation with valid and invalid values."""
    # Valid values
    assert (
        PoolSettings(SERVER_MONITORING_MODE="auto").SERVER_MONITORING_MODE
        == "auto"
    )
    assert (
        PoolSettings(SERVER_MONITORING_MODE="stream").SERVER_MONITORING_MODE
        == "stream"
    )
    assert (
        PoolSettings(SERVER_MONITORING_MODE="poll").SERVER_MONITORING_MODE
        == "poll"
    )

    # Invalid values
    with pytest.raises(ValidationError):
        PoolSettings(SERVER_MONITORING_MODE="invalid")
    with pytest.raises(ValidationError):
        PoolSettings(SERVER_MONITORING_MODE="")
    with pytest.raises(ValidationError):
        PoolSettings(SERVER_MONITORING_MODE="Auto")  # Case sensitive


def test_pool_settings_client_kwargs_all_fields_set() -> None:
    """Test client_kwargs returns all fields when all values are set."""
    settings = PoolSettings(
        MAX_SIZE=500,
        MIN_SIZE=10,
        MAX_IDLE_TIME_MS=30000,
        MAX_CONNECTING=50,
        WAIT_QUEUE_TIMEOUT_MS=15000,
        HEARTBEAT_FREQUENCY_MS=5000,
        SERVER_MONITORING_MODE="poll",
    )

    expected: dict[str, Any] = {
        "maxPoolSize": 500,
        "minPoolSize": 10,
        "maxIdleTimeMS": 30000,
        "maxConnecting": 50,
        "waitQueueTimeoutMS": 15000,
        "heartbeatFrequencyMS": 5000,
        "serverMonitoringMode": "poll",
    }

    assert settings.client_kwargs == expected


def test_pool_settings_client_kwargs_no_fields_set() -> None:
    """Test client_kwargs returns empty dict when all values are None."""
    settings = PoolSettings(
        MAX_SIZE=None,
        MIN_SIZE=None,
        MAX_IDLE_TIME_MS=None,
        MAX_CONNECTING=None,
        WAIT_QUEUE_TIMEOUT_MS=None,
        HEARTBEAT_FREQUENCY_MS=None,
        SERVER_MONITORING_MODE=None,
    )

    assert settings.client_kwargs == {}


def test_pool_settings_client_kwargs_partial_fields_set() -> None:
    """Test client_kwargs returns only set fields."""
    # Test with only MAX_SIZE and MAX_IDLE_TIME_MS set
    settings = PoolSettings(
        MAX_SIZE=500,
        MIN_SIZE=None,
        MAX_IDLE_TIME_MS=30000,
        MAX_CONNECTING=None,
        WAIT_QUEUE_TIMEOUT_MS=None,
        HEARTBEAT_FREQUENCY_MS=None,
        SERVER_MONITORING_MODE=None,
    )

    expected: dict[str, Any] = {
        "maxPoolSize": 500,
        "maxIdleTimeMS": 30000,
    }

    assert settings.client_kwargs == expected

    # Test with only MIN_SIZE and WAIT_QUEUE_TIMEOUT_MS set
    settings = PoolSettings(
        MAX_SIZE=None,
        MIN_SIZE=10,
        MAX_IDLE_TIME_MS=None,
        MAX_CONNECTING=None,
        WAIT_QUEUE_TIMEOUT_MS=15000,
        HEARTBEAT_FREQUENCY_MS=None,
        SERVER_MONITORING_MODE=None,
    )

    expected = {
        "minPoolSize": 10,
        "waitQueueTimeoutMS": 15000,
    }

    assert settings.client_kwargs == expected

    # Test with only SERVER_MONITORING_MODE set
    settings = PoolSettings(
        MAX_SIZE=None,
        MIN_SIZE=None,
        MAX_IDLE_TIME_MS=None,
        MAX_CONNECTING=None,
        WAIT_QUEUE_TIMEOUT_MS=None,
        HEARTBEAT_FREQUENCY_MS=None,
        SERVER_MONITORING_MODE="stream",
    )

    expected = {
        "serverMonitoringMode": "stream",
    }

    assert settings.client_kwargs == expected


def test_pool_settings_client_kwargs_zero_values_included() -> None:
    """Test that zero values are included in client_kwargs since they are valid settings."""
    # Test with zero values (these are valid for non-negative integers)
    settings = PoolSettings(
        MAX_SIZE=100,
        MIN_SIZE=0,
        MAX_IDLE_TIME_MS=0,
        MAX_CONNECTING=5,
        WAIT_QUEUE_TIMEOUT_MS=0,
        HEARTBEAT_FREQUENCY_MS=0,
        SERVER_MONITORING_MODE="auto",
    )

    expected: dict[str, Any] = {
        "maxPoolSize": 100,
        "minPoolSize": 0,
        "maxIdleTimeMS": 0,
        "maxConnecting": 5,
        "waitQueueTimeoutMS": 0,
        "heartbeatFrequencyMS": 0,
        "serverMonitoringMode": "auto",
    }

    assert settings.client_kwargs == expected
