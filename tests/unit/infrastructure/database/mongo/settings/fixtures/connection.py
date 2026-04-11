from collections.abc import Callable
from typing import Any

import pytest
from pydantic import MongoDsn

from src.infrastructure.database.mongo.settings.connection import (
    ConnectionSettings,
)
from src.infrastructure.database.mongo.settings.constants import (
    ConnectionDefaults as Defaults,
)


@pytest.fixture(name="default_connection_settings")
def default() -> ConnectionSettings:
    return ConnectionSettings(USERNAME=Defaults.USERNAME)


@pytest.fixture(name="custom_connection_settings")
def custom() -> Callable[[dict[str, Any]], ConnectionSettings]:
    def _custom(**kwargs: Any) -> ConnectionSettings:
        return ConnectionSettings(**kwargs)

    return _custom


@pytest.fixture(name="default_dsn")
def dsn() -> MongoDsn:
    return MongoDsn.build(
        host=Defaults.HOST,
        port=Defaults.PORT,
        scheme=Defaults.SCHEMA,
        username=Defaults.USERNAME,
        password=Defaults.PASSWORD,
    )
