from collections.abc import Callable
from typing import Any

import pytest

from src.infrastructure.database.mongo.settings.tls import (
    TLSSettings,
)


@pytest.fixture(name="default_tls_settings")
def default() -> TLSSettings:
    return TLSSettings()


@pytest.fixture(name="custom_tls_settings")
def custom() -> Callable[[dict[str, Any]], TLSSettings]:
    def _custom(**kwargs: Any) -> TLSSettings:
        return TLSSettings(**kwargs)

    return _custom


@pytest.fixture(name="default_tls_client_kwargs")
def default_client_kwargs() -> dict[str, Any]:
    return {}
