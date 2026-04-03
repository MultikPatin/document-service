from beanie import PydanticObjectId
from bson.errors import InvalidId

from src.core.constants import CURSOR_SEPARATOR
from src.infra.db.mongo.exceptions import InvalidMongoIDError


def to_mongo_id(_id: str) -> PydanticObjectId:
    s = _id.split(CURSOR_SEPARATOR, 1)
    try:
        if len(s) == 1:
            return PydanticObjectId(_id)
        return PydanticObjectId(s[-1])
    except InvalidId as e:
        raise InvalidMongoIDError(_id) from e
