import pytest

from src.infrastructure.database.mongo.settings.srv import SRVSettings


@pytest.fixture
def default_srv_settings() -> SRVSettings:
    """Fixture that returns SRVSettings with default values."""
    return SRVSettings()


@pytest.fixture
def custom_srv_settings() -> SRVSettings:
    """Fixture that returns SRVSettings with custom values."""
    return SRVSettings(SERVICE_NAME="customService", MAX_HOSTS=15)
