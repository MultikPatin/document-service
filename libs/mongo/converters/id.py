from collections.abc import Sequence

from beanie import PydanticObjectId
from bson.errors import InvalidId

from libs.mongo.constants.converters import CURSOR_SEPARATOR
from libs.mongo.exceptions import InvalidMongoIDError


def to_poid(_id: str, /) -> PydanticObjectId:
    s = _id.split(CURSOR_SEPARATOR, 1)
    try:
        if len(s) == 1:
            return PydanticObjectId(_id)
        return PydanticObjectId(s[-1])
    except InvalidId as e:
        raise InvalidMongoIDError(_id) from e


def to_poids(ids: Sequence[str], /) -> Sequence[PydanticObjectId]:
    return [to_poid(i) for i in ids]
