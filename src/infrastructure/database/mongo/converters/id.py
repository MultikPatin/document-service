from beanie import PydanticObjectId
from bson.errors import InvalidId

from src.infrastructure.database.mongo.exceptions import InvalidMongoIDError

from .constants import CURSOR_SEPARATOR


def to_poid(_id: str, /) -> PydanticObjectId:
    s = _id.split(CURSOR_SEPARATOR, 1)
    try:
        if len(s) == 1:
            return PydanticObjectId(_id)
        return PydanticObjectId(s[-1])
    except InvalidId as e:
        raise InvalidMongoIDError(_id) from e
