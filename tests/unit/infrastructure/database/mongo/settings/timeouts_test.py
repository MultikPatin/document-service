from typing import Any

import pytest
from pydantic import ValidationError

from src.infrastructure.database.mongo.settings.constants import (
    TimeoutsDefaults,
)
from src.infrastructure.database.mongo.settings.timeouts import TimeoutsSettings


def test_timeouts_settings_default_values() -> None:
    """Test that TimeoutsSettings uses default values from TimeoutsDefaults when no values are provided."""
    # Arrange
    expected_connection_ms = TimeoutsDefaults.CONNECTION_MS
    expected_socket_ms = TimeoutsDefaults.SOCKET_MS
    expected_server_selection_ms = TimeoutsDefaults.SERVER_SELECTION_MS
    expected_operation_ms = TimeoutsDefaults.OPERATION_MS

    # Act
    settings = TimeoutsSettings()

    # Assert
    assert expected_connection_ms == settings.CONNECTION_MS
    assert expected_socket_ms == settings.SOCKET_MS
    assert expected_server_selection_ms == settings.SERVER_SELECTION_MS
    assert expected_operation_ms == settings.OPERATION_MS


def test_timeouts_settings_custom_values() -> None:
    """Test that TimeoutsSettings properly sets custom values for all timeout fields."""
    # Arrange
    connection_ms = 5000
    socket_ms = 15000
    server_selection_ms = 25000
    operation_ms = 35000

    # Act
    settings = TimeoutsSettings(
        CONNECTION_MS=connection_ms,
        SOCKET_MS=socket_ms,
        SERVER_SELECTION_MS=server_selection_ms,
        OPERATION_MS=operation_ms,
    )

    # Assert
    assert connection_ms == settings.CONNECTION_MS
    assert socket_ms == settings.SOCKET_MS
    assert server_selection_ms == settings.SERVER_SELECTION_MS
    assert operation_ms == settings.OPERATION_MS


def test_timeouts_settings_client_kwargs_structure() -> None:
    """Test that client_kwargs property returns a dictionary with the correct structure and values."""
    # Arrange
    connection_ms = 5000
    socket_ms = 15000
    server_selection_ms = 25000
    operation_ms = 35000

    # Act
    settings = TimeoutsSettings(
        CONNECTION_MS=connection_ms,
        SOCKET_MS=socket_ms,
        SERVER_SELECTION_MS=server_selection_ms,
        OPERATION_MS=operation_ms,
    )
    client_kwargs: dict[str, Any] = settings.client_kwargs

    # Assert
    assert isinstance(client_kwargs, dict)
    assert "connectTimeoutMS" in client_kwargs
    assert "socketTimeoutMS" in client_kwargs
    assert "serverSelectionTimeoutMS" in client_kwargs
    assert "timeoutMS" in client_kwargs
    assert client_kwargs["connectTimeoutMS"] == connection_ms
    assert client_kwargs["socketTimeoutMS"] == socket_ms
    assert client_kwargs["serverSelectionTimeoutMS"] == server_selection_ms
    assert client_kwargs["timeoutMS"] == operation_ms


def test_timeouts_settings_client_kwargs_with_operation_timeout() -> None:
    """Test that client_kwargs includes 'timeoutMS' when OPERATION_MS has a value."""
    # Arrange
    operation_ms = 35000

    # Act
    settings = TimeoutsSettings(OPERATION_MS=operation_ms)
    client_kwargs: dict[str, Any] = settings.client_kwargs

    # Assert
    assert "timeoutMS" in client_kwargs
    assert client_kwargs["timeoutMS"] == operation_ms


def test_timeouts_settings_client_kwargs_without_operation_timeout() -> None:
    """Test that client_kwargs does not include 'timeoutMS' when OPERATION_MS is None."""
    # Arrange
    operation_ms = None

    # Act
    settings = TimeoutsSettings(OPERATION_MS=operation_ms)
    client_kwargs: dict[str, Any] = settings.client_kwargs

    # Assert
    assert "timeoutMS" not in client_kwargs


def test_timeouts_settings_client_kwargs_returns_dict() -> None:
    """Test that client_kwargs property returns a dictionary type."""
    # Arrange
    settings = TimeoutsSettings()

    # Act & Assert
    assert isinstance(settings.client_kwargs, dict)


def test_timeouts_settings_validation_non_negative_integers() -> None:
    """Test that TimeoutsSettings accepts valid non-negative integer values for all timeout fields."""
    # Test with zero
    # Arrange
    connection_ms_zero = 0
    socket_ms_zero = 0
    server_selection_ms_zero = 0
    operation_ms_zero = 0

    # Act
    settings_zero = TimeoutsSettings(
        CONNECTION_MS=connection_ms_zero,
        SOCKET_MS=socket_ms_zero,
        SERVER_SELECTION_MS=server_selection_ms_zero,
        OPERATION_MS=operation_ms_zero,
    )

    # Assert
    assert connection_ms_zero == settings_zero.CONNECTION_MS
    assert socket_ms_zero == settings_zero.SOCKET_MS
    assert server_selection_ms_zero == settings_zero.SERVER_SELECTION_MS
    assert operation_ms_zero == settings_zero.OPERATION_MS

    # Test with positive values
    # Arrange
    connection_ms_positive = 1000
    socket_ms_positive = 2000
    server_selection_ms_positive = 3000
    operation_ms_positive = 4000

    # Act
    settings_positive = TimeoutsSettings(
        CONNECTION_MS=connection_ms_positive,
        SOCKET_MS=socket_ms_positive,
        SERVER_SELECTION_MS=server_selection_ms_positive,
        OPERATION_MS=operation_ms_positive,
    )

    # Assert
    assert connection_ms_positive == settings_positive.CONNECTION_MS
    assert socket_ms_positive == settings_positive.SOCKET_MS
    assert server_selection_ms_positive == settings_positive.SERVER_SELECTION_MS
    assert operation_ms_positive == settings_positive.OPERATION_MS


def test_timeouts_settings_validation_negative_values() -> None:
    """Test that TimeoutsSettings raises ValidationError for negative values in all timeout fields."""
    # Arrange
    negative_value = -1

    # Assert
    with pytest.raises(ValidationError):
        TimeoutsSettings(CONNECTION_MS=negative_value)

    with pytest.raises(ValidationError):
        TimeoutsSettings(SOCKET_MS=negative_value)

    with pytest.raises(ValidationError):
        TimeoutsSettings(SERVER_SELECTION_MS=negative_value)

    with pytest.raises(ValidationError):
        TimeoutsSettings(OPERATION_MS=negative_value)
