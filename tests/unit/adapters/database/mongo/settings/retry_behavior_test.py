from typing import Any

import pytest
from libs.mongo.constants.settings import (
    RetryBehaviorDefaults as D,
)
from libs.mongo.settings.retry_behavior import (
    RetryBehaviorSettings,
)


def test_retry_behavior_settings_default(
    default_retry_behavior_settings, default_retry_behavior_client_kwargs
) -> None:
    """Test default values for RepresentationSettings."""
    s = default_retry_behavior_settings

    assert s.WRITES == D.WRITES
    assert s.READS == D.READS
    assert s.client_kwargs == default_retry_behavior_client_kwargs


def test_retry_behavior_settings_client_kwargs_returns_dict() -> None:
    """Test that client_kwargs property returns a dictionary type."""
    settings = RetryBehaviorSettings()

    assert isinstance(settings.client_kwargs, dict)


@pytest.mark.parametrize(
    ("writes", "reads", "expected_writes", "expected_reads"),
    [
        (True, True, True, True),
        (True, False, True, False),
        (False, True, False, True),
        (False, False, False, False),
    ],
)
def test_retry_behavior_settings_values(
    writes, reads, expected_writes, expected_reads
) -> None:
    """Test RetryBehaviorSettings with various combinations of WRITES and READS values."""
    settings = RetryBehaviorSettings(WRITES=writes, READS=reads)

    assert expected_writes == settings.WRITES
    assert expected_reads == settings.READS


@pytest.mark.parametrize(
    ("writes", "reads", "expected_retry_writes", "expected_retry_reads"),
    [
        (True, True, True, True),
        (True, False, True, False),
        (False, True, False, True),
        (False, False, False, False),
    ],
)
def test_retry_behavior_settings_client_kwargs_structure(
    writes, reads, expected_retry_writes, expected_retry_reads
) -> None:
    """Test that client_kwargs property returns a dictionary with the correct structure and values for various input combinations."""
    settings = RetryBehaviorSettings(WRITES=writes, READS=reads)

    client_kwargs: dict[str, Any] = settings.client_kwargs

    assert isinstance(client_kwargs, dict)
    assert "retryWrites" in client_kwargs
    assert "retryReads" in client_kwargs
    assert client_kwargs["retryWrites"] is expected_retry_writes
    assert client_kwargs["retryReads"] is expected_retry_reads
