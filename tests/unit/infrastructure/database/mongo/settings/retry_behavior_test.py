from src.infrastructure.database.mongo.settings.constants import (
    RetryBehaviorDefaults,
)
from src.infrastructure.database.mongo.settings.retry_behavior import (
    RetryBehaviorSettings,
)


def test_retry_behavior_settings_default_values() -> None:
    """Test that RetryBehaviorSettings uses default values from RetryBehaviorDefaults when no values are provided."""
    settings = RetryBehaviorSettings()

    assert settings.WRITES == RetryBehaviorDefaults.WRITES
    assert settings.READS == RetryBehaviorDefaults.READS


def test_retry_behavior_settings_custom_values() -> None:
    """Test that RetryBehaviorSettings properly sets custom values for WRITES and READS."""
    settings = RetryBehaviorSettings(WRITES=False, READS=True)

    assert settings.WRITES is False
    assert settings.READS is True


def test_retry_behavior_settings_client_kwargs_structure() -> None:
    """Test that client_kwargs property returns a dictionary with the correct structure and values."""
    settings = RetryBehaviorSettings(WRITES=True, READS=False)

    client_kwargs = settings.client_kwargs

    assert isinstance(client_kwargs, dict)
    assert "retryWrites" in client_kwargs
    assert "retryReads" in client_kwargs
    assert client_kwargs["retryWrites"] is True
    assert client_kwargs["retryReads"] is False


def test_retry_behavior_settings_client_kwargs_returns_dict() -> None:
    """Test that client_kwargs property returns a dictionary type."""
    settings = RetryBehaviorSettings()

    assert isinstance(settings.client_kwargs, dict)
