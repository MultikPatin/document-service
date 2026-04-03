import pytest
from beanie import PydanticObjectId

from src.core.constants import CURSOR_SEPARATOR
from src.infra.db.mongo.convs.id import to_poid
from src.infra.db.mongo.exceptions import InvalidMongoIDError


@pytest.fixture
def valid_id() -> str:
    return str(PydanticObjectId())


@pytest.fixture
def invalid_id() -> str:
    return "not-a-valid-object-id"


@pytest.fixture
def prefix() -> str:
    return "prefix"


def test_convert_to_id_valid(valid_id):
    """Test converting a valid single ID string."""
    expected_object_id = PydanticObjectId(valid_id)
    result = to_poid(valid_id)
    assert isinstance(result, PydanticObjectId)
    assert result == expected_object_id


def test_convert_to_id_with_cursor(valid_id, prefix):
    """Test converting an ID with cursor separator, using last part."""
    cursor = f"{prefix}{CURSOR_SEPARATOR}{valid_id}"
    expected_object_id = PydanticObjectId(valid_id)
    result = to_poid(cursor)
    assert isinstance(result, PydanticObjectId)
    assert result == expected_object_id


def test_convert_to_id_invalid_after_first_split(valid_id, prefix):
    """Test converting an ID where the part after first separator is not a valid ObjectId."""
    invalid_cursor = (
        f"{prefix}{CURSOR_SEPARATOR}{prefix}{CURSOR_SEPARATOR}{valid_id}"
    )
    with pytest.raises(InvalidMongoIDError):
        to_poid(invalid_cursor)


def test_convert_to_id_empty_string():
    """Test converting an empty string."""
    empty_id = ""
    with pytest.raises(InvalidMongoIDError):
        to_poid(empty_id)


def test_convert_to_id_invalid_object_id(invalid_id):
    """Test converting an invalid ObjectId format."""
    with pytest.raises(InvalidMongoIDError):
        to_poid(invalid_id)


def test_convert_to_id_none_input():
    """Test converting None input (should raise AttributeError)."""
    with pytest.raises(AttributeError):
        to_poid(None)  # type: ignore
