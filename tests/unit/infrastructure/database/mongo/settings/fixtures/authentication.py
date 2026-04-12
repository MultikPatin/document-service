from collections.abc import Callable
from typing import Any

import pytest

from src.infrastructure.database.mongo.settings.authentication import (
    AuthenticationSettings,
)
from src.infrastructure.database.mongo.settings.constants import (
    AuthenticationDefaults as D,
)
from src.infrastructure.database.mongo.settings.constants import (
    AuthenticationKeys as K,
)


@pytest.fixture(name="default_authentication_settings")
def default() -> AuthenticationSettings:
    return AuthenticationSettings()


@pytest.fixture(name="custom_authentication_settings")
def custom() -> Callable[[dict[str, Any]], AuthenticationSettings]:
    def _custom(**kwargs: Any) -> AuthenticationSettings:
        return AuthenticationSettings(**kwargs)

    return _custom


@pytest.fixture(name="default_authentication_client_kwargs")
def default_client_kwargs() -> dict[str, Any]:
    return {K.SOURCE: D.SOURCE, K.MECHANISM: D.MECHANISM}
