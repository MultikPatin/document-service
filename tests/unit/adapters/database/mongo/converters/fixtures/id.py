import pytest
from beanie import PydanticObjectId


@pytest.fixture
def valid_id() -> str:
    return str(PydanticObjectId())


@pytest.fixture
def invalid_id() -> str:
    return "not-a-valid-object-id"


@pytest.fixture
def prefix() -> str:
    return "prefix"
