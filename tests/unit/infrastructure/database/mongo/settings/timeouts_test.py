import pytest
from pydantic import ValidationError

from src.infrastructure.database.mongo.settings.constants import (
    TimeoutsDefaults as D,
)
from src.infrastructure.database.mongo.settings.timeouts import TimeoutsSettings


def test_timeouts_settings_default(
    default_timeouts_settings, default_timeouts_client_kwargs
) -> None:
    """Test default values for TimeoutsSettings."""
    s = default_timeouts_settings

    assert s.CONNECTION_MS == D.CONNECTION
    assert s.SOCKET_MS == D.SOCKET
    assert s.SERVER_SELECTION_MS == D.SERVER_SELECTION
    assert s.OPERATION_MS == D.OPERATION
    assert s.client_kwargs == default_timeouts_client_kwargs


@pytest.mark.parametrize(
    ("connection_ms", "socket_ms", "server_selection_ms", "operation_ms"),
    [
        (
            D.CONNECTION,
            D.SOCKET,
            D.SERVER_SELECTION,
            D.OPERATION,
        ),
        (5000, 15000, 25000, 35000),
    ],
)
def test_timeouts_settings_values(
    timeouts_settings: TimeoutsSettings,
    connection_ms: int,
    socket_ms: int,
    server_selection_ms: int,
    operation_ms: int | None,
) -> None:
    """Test that TimeoutsSettings properly sets values for all timeout fields with both default and custom values."""
    # Arrange
    settings = TimeoutsSettings(
        CONNECTION_MS=connection_ms,
        SOCKET_MS=socket_ms,
        SERVER_SELECTION_MS=server_selection_ms,
        OPERATION_MS=operation_ms,
    )

    # Act & Assert
    assert connection_ms == settings.CONNECTION_MS
    assert socket_ms == settings.SOCKET_MS
    assert server_selection_ms == settings.SERVER_SELECTION_MS
    assert operation_ms == settings.OPERATION_MS


@pytest.mark.parametrize(
    ("connection_ms", "socket_ms", "server_selection_ms", "operation_ms"),
    [
        (5000, 15000, 25000, 35000),
        (0, 0, 0, 0),
        (1000, 2000, 3000, 4000),
    ],
)
def test_timeouts_settings_client_kwargs_structure(
    connection_ms: int,
    socket_ms: int,
    server_selection_ms: int,
    operation_ms: int | None,
) -> None:
    """Test that client_kwargs property returns a dictionary with the correct structure and values for various timeout configurations."""
    # Arrange
    settings = TimeoutsSettings(
        CONNECTION_MS=connection_ms,
        SOCKET_MS=socket_ms,
        SERVER_SELECTION_MS=server_selection_ms,
        OPERATION_MS=operation_ms,
    )

    # Act
    client_kwargs = settings.client_kwargs

    # Assert
    assert isinstance(client_kwargs, dict)
    assert "connectTimeoutMS" in client_kwargs
    assert "socketTimeoutMS" in client_kwargs
    assert "serverSelectionTimeoutMS" in client_kwargs
    assert client_kwargs["connectTimeoutMS"] == connection_ms
    assert client_kwargs["socketTimeoutMS"] == socket_ms
    assert client_kwargs["serverSelectionTimeoutMS"] == server_selection_ms

    if operation_ms is not None and operation_ms > 0:
        assert "timeoutMS" in client_kwargs
        assert client_kwargs["timeoutMS"] == operation_ms
    else:
        assert "timeoutMS" not in client_kwargs


@pytest.mark.parametrize(
    "value",
    [0, 1000, 5000, 10000],
)
def test_timeouts_settings_validation_non_negative_integers(
    timeouts_settings: TimeoutsSettings,
    value: int,
) -> None:
    """Test that TimeoutsSettings accepts valid non-negative integer values for all timeout fields."""
    # Act & Assert
    settings = TimeoutsSettings(
        CONNECTION_MS=value,
        SOCKET_MS=value,
        SERVER_SELECTION_MS=value,
        OPERATION_MS=value,
    )
    assert value == settings.CONNECTION_MS
    assert value == settings.SOCKET_MS
    assert value == settings.SERVER_SELECTION_MS
    assert value == settings.OPERATION_MS


@pytest.mark.parametrize(
    "field_name",
    ["CONNECTION_MS", "SOCKET_MS", "SERVER_SELECTION_MS", "OPERATION_MS"],
)
def test_timeouts_settings_validation_negative_values(field_name: str) -> None:
    """Test that TimeoutsSettings raises ValidationError for negative values in all timeout fields."""
    # Arrange
    negative_value = -1
    kwargs = {field_name: negative_value}

    # Act & Assert
    with pytest.raises(ValidationError):
        TimeoutsSettings(**kwargs)
