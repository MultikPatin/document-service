from typing import Any

import pytest
from pydantic import ValidationError

from libs.mongo.constants.settings import (
    PoolDefaults as D,
)
from libs.mongo.settings.pool import PoolSettings


def test_pool_settings_default(
    default_pool_settings, default_pool_client_kwargs
) -> None:
    """Test default values for PoolSettings."""
    s = default_pool_settings

    assert s.MAX_SIZE == D.MAX_SIZE
    assert s.MIN_SIZE == D.MIN_SIZE
    assert s.MAX_IDLE_TIME_MS == D.MAX_IDLE_TIME
    assert s.MAX_CONNECTING == D.MAX_CONNECTING
    assert s.WAIT_QUEUE_TIMEOUT_MS == D.WAIT_QUEUE_TIMEOUT
    assert s.HEARTBEAT_FREQUENCY_MS == D.HEARTBEAT_FREQUENCY
    assert s.SERVER_MONITORING_MODE == D.SERVER_MONITORING_MODE
    assert s.client_kwargs == default_pool_client_kwargs


@pytest.mark.parametrize(
    (
        "max_size",
        "min_size",
        "max_idle_time_ms",
        "max_connecting",
        "wait_queue_timeout_ms",
        "heartbeat_frequency_ms",
        "server_monitoring_mode",
    ),
    [
        (
            D.MAX_SIZE,
            D.MIN_SIZE,
            D.MAX_IDLE_TIME,
            D.MAX_CONNECTING,
            D.WAIT_QUEUE_TIMEOUT,
            D.HEARTBEAT_FREQUENCY,
            D.SERVER_MONITORING_MODE,
        ),
        (
            500,
            10,
            30000,
            50,
            15000,
            5000,
            "poll",
        ),
    ],
    ids=["default-values", "custom-values"],
)
def test_pool_settings_with_valid_values(  # noqa: PLR0913
    max_size: int | None,
    min_size: int | None,
    max_idle_time_ms: int | None,
    max_connecting: int | None,
    wait_queue_timeout_ms: int | None,
    heartbeat_frequency_ms: int | None,
    server_monitoring_mode: str | None,
) -> None:
    """Test PoolSettings with valid values for all fields."""
    settings = PoolSettings(
        MAX_SIZE=max_size,
        MIN_SIZE=min_size,
        MAX_IDLE_TIME_MS=max_idle_time_ms,
        MAX_CONNECTING=max_connecting,
        WAIT_QUEUE_TIMEOUT_MS=wait_queue_timeout_ms,
        HEARTBEAT_FREQUENCY_MS=heartbeat_frequency_ms,
        SERVER_MONITORING_MODE=server_monitoring_mode,
    )

    assert max_size == settings.MAX_SIZE
    assert min_size == settings.MIN_SIZE
    assert max_idle_time_ms == settings.MAX_IDLE_TIME_MS
    assert max_connecting == settings.MAX_CONNECTING
    assert wait_queue_timeout_ms == settings.WAIT_QUEUE_TIMEOUT_MS
    assert heartbeat_frequency_ms == settings.HEARTBEAT_FREQUENCY_MS
    assert server_monitoring_mode == settings.SERVER_MONITORING_MODE


@pytest.mark.parametrize(
    "field_name",
    [
        "MAX_SIZE",
        "MIN_SIZE",
        "MAX_IDLE_TIME_MS",
        "MAX_CONNECTING",
        "WAIT_QUEUE_TIMEOUT_MS",
        "HEARTBEAT_FREQUENCY_MS",
        "SERVER_MONITORING_MODE",
    ],
    ids=[
        "max-size-none",
        "min-size-none",
        "max-idle-time-ms-none",
        "max-connecting-none",
        "wait-queue-timeout-ms-none",
        "heartbeat-frequency-ms-none",
        "server-monitoring-mode-none",
    ],
)
def test_pool_settings_accepts_none_values(field_name: str) -> None:
    """Test that PoolSettings accepts None for all optional fields."""
    # Create a dictionary with all fields set to None
    kwargs = {
        "MAX_SIZE": None,
        "MIN_SIZE": None,
        "MAX_IDLE_TIME_MS": None,
        "MAX_CONNECTING": None,
        "WAIT_QUEUE_TIMEOUT_MS": None,
        "HEARTBEAT_FREQUENCY_MS": None,
        "SERVER_MONITORING_MODE": None,
    }

    settings = PoolSettings(**kwargs)

    # Get the actual value from settings using getattr
    actual_value = getattr(settings, field_name)
    assert actual_value is None


@pytest.mark.parametrize(
    "max_size",
    [1, D.MAX_SIZE],
    ids=["max-size-minimum", "max-size-default"],
)
def test_pool_settings_with_valid_max_size_values(max_size: int) -> None:
    """Test PoolSettings with valid boundary values for MAX_SIZE."""
    settings = PoolSettings(MAX_SIZE=max_size)
    assert max_size == settings.MAX_SIZE


@pytest.mark.parametrize(
    "max_size",
    [0, 1001, -1],
    ids=["max-size-zero", "max-size-too-large", "max-size-negative"],
)
def test_pool_settings_validation_error_invalid_max_size(max_size: int) -> None:
    """Test ValidationError for invalid MAX_SIZE values."""
    with pytest.raises(ValidationError):
        PoolSettings(MAX_SIZE=max_size)


@pytest.mark.parametrize(
    "min_size",
    [0, D.MIN_SIZE],
    ids=["min-size-zero", "min-size-default"],
)
def test_pool_settings_with_valid_min_size_values(min_size: int) -> None:
    """Test PoolSettings with valid boundary values for MIN_SIZE."""
    settings = PoolSettings(MIN_SIZE=min_size)
    assert min_size == settings.MIN_SIZE


@pytest.mark.parametrize(
    "min_size",
    [-1, 1000],
    ids=["min-size-negative", "min-size-too-large"],
)
def test_pool_settings_validation_error_invalid_min_size(min_size: int) -> None:
    """Test ValidationError for invalid MIN_SIZE values."""
    with pytest.raises(ValidationError):
        PoolSettings(MIN_SIZE=min_size)


@pytest.mark.parametrize(
    "max_connecting",
    [1, D.MAX_CONNECTING],
    ids=["max-connecting-minimum", "max-connecting-default"],
)
def test_pool_settings_with_valid_max_connecting_values(
    max_connecting: int,
) -> None:
    """Test PoolSettings with valid boundary values for MAX_CONNECTING."""
    settings = PoolSettings(MAX_CONNECTING=max_connecting)
    assert max_connecting == settings.MAX_CONNECTING


@pytest.mark.parametrize(
    "max_connecting",
    [0, 101, -1],
    ids=[
        "max-connecting-zero",
        "max-connecting-too-large",
        "max-connecting-negative",
    ],
)
def test_pool_settings_validation_error_invalid_max_connecting(
    max_connecting: int,
) -> None:
    """Test ValidationError for invalid MAX_CONNECTING values."""
    with pytest.raises(ValidationError):
        PoolSettings(MAX_CONNECTING=max_connecting)


@pytest.mark.parametrize(
    "server_monitoring_mode",
    ["auto", "stream", "poll"],
    ids=[
        "server-monitoring-mode-auto",
        "server-monitoring-mode-stream",
        "server-monitoring-mode-poll",
    ],
)
def test_pool_settings_with_valid_server_monitoring_mode_values(
    server_monitoring_mode: str,
) -> None:
    """Test PoolSettings with valid values for SERVER_MONITORING_MODE."""
    settings = PoolSettings(SERVER_MONITORING_MODE=server_monitoring_mode)
    assert server_monitoring_mode == settings.SERVER_MONITORING_MODE


@pytest.mark.parametrize(
    "server_monitoring_mode",
    ["invalid", "", "Auto"],
    ids=[
        "server-monitoring-mode-invalid",
        "server-monitoring-mode-empty",
        "server-monitoring-mode-wrong-case",
    ],
)
def test_pool_settings_validation_error_invalid_server_monitoring_mode(
    server_monitoring_mode: str,
) -> None:
    """Test ValidationError for invalid SERVER_MONITORING_MODE values."""
    with pytest.raises(ValidationError):
        PoolSettings(SERVER_MONITORING_MODE=server_monitoring_mode)


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
        MAX_IDLE_TIME_MS=1,
        MAX_CONNECTING=5,
        WAIT_QUEUE_TIMEOUT_MS=1,
        HEARTBEAT_FREQUENCY_MS=0,
        SERVER_MONITORING_MODE="auto",
    )

    expected: dict[str, Any] = {
        "maxPoolSize": 100,
        "minPoolSize": 0,
        "maxIdleTimeMS": 1,
        "maxConnecting": 5,
        "waitQueueTimeoutMS": 1,
        "heartbeatFrequencyMS": 0,
        "serverMonitoringMode": "auto",
    }

    assert settings.client_kwargs == expected
