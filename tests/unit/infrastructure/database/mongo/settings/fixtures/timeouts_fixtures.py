import pytest

from src.infrastructure.database.mongo.settings.timeouts import TimeoutsSettings


@pytest.fixture
def timeouts_settings() -> TimeoutsSettings:
    """Fixture for TimeoutsSettings with default values."""
    return TimeoutsSettings()
