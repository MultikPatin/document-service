from collections.abc import Callable
from typing import Any

import pytest

from libs.mongo.constants.settings import (
    AuthenticationDefaults as D,
)
from libs.mongo.constants.settings import (
    AuthenticationKeys as K,
)
from libs.mongo.settings.authentication import (
    AuthenticationSettings,
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
