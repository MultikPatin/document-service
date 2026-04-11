from collections.abc import Callable
from typing import Any

import pytest

from src.infrastructure.database.mongo.settings.constants import (
    RepresentationDefaults as D,
)
from src.infrastructure.database.mongo.settings.constants import (
    RepresentationKeys as K,
)
from src.infrastructure.database.mongo.settings.representation import (
    RepresentationSettings,
)


@pytest.fixture(name="default_representation_settings")
def default() -> RepresentationSettings:
    return RepresentationSettings()


@pytest.fixture(name="custom_representation_settings")
def custom() -> Callable[[dict[str, Any]], RepresentationSettings]:
    def _custom(**kwargs: Any) -> RepresentationSettings:
        return RepresentationSettings(**kwargs)

    return _custom


@pytest.fixture(name="default_representation_client_kwargs")
def default_client_kwargs() -> dict[str, Any]:
    return {K.UUID: D.UUID}
