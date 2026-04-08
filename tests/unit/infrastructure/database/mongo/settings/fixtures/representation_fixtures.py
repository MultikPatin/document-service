from typing import Any

import pytest

from src.infrastructure.database.mongo.settings.constants import (
    RepresentationDefaults,
)


@pytest.fixture
def expected_client_kwargs() -> dict[str, Any]:
    """Fixture that returns expected client_kwargs for different UUID representations."""
    return {"uuidRepresentation": RepresentationDefaults.UUID}
