from collections.abc import Callable
from typing import Any

import pytest

from libs.mongo.constants.settings import (
    SRVDefaults as D,
)
from libs.mongo.constants.settings import (
    SRVKeys as K,
)
from libs.mongo.settings.srv import (
    SRVSettings,
)


@pytest.fixture(name="default_srv_settings")
def default() -> SRVSettings:
    return SRVSettings()


@pytest.fixture(name="custom_srv_settings")
def custom() -> Callable[[dict[str, Any]], SRVSettings]:
    def _custom(**kwargs: Any) -> SRVSettings:
        return SRVSettings(**kwargs)

    return _custom


@pytest.fixture(name="default_srv_client_kwargs")
def default_client_kwargs() -> dict[str, Any]:
    return {K.SERVICE_NAME: D.SERVICE_NAME, K.MAX_HOSTS: D.MAX_HOSTS}
