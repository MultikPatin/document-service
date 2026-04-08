import pytest

from src.infrastructure.database.mongo.settings.write_concern import (
    WriteConcernSettings,
)


@pytest.fixture
def default_write_concern_settings() -> WriteConcernSettings:
    """Fixture providing WriteConcernSettings with default values."""
    return WriteConcernSettings()
