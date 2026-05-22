from collections.abc import Iterable
from typing import TYPE_CHECKING

from beanie import PydanticObjectId
from beanie.odm.enums import SortDirection
from bson.errors import InvalidId

from src.domain.constants import CURSOR_SEPARATOR, SORT_DESC_PREFIX
from src.infra.mongo.errors import InvalidIDFormatError, InvalidSortError

if TYPE_CHECKING:
    from src.infra.mongo.annotations import QuerySortType


def to_id(id_: str) -> PydanticObjectId:
    s = id_.split(CURSOR_SEPARATOR, 1)
    try:
        if len(s) == 1:
            return PydanticObjectId(id_)
        return PydanticObjectId(s[-1])
    except InvalidId as e:
        raise InvalidIDFormatError(id_) from e


def prepare_sort(
    document: object, sort: str | Iterable[str] | None
) -> QuerySortType:
    if sort is None:
        return None
    if isinstance(sort, str):
        return [_split_sort(document, sort)]
    if isinstance(sort, Iterable):
        return [_split_sort(document, s) for s in sort]
    raise InvalidSortError(sort)


def _split_sort(document: object, sort: str) -> tuple[str, SortDirection]:
    if sort.startswith(SORT_DESC_PREFIX):
        s = sort.removeprefix(SORT_DESC_PREFIX), SortDirection.DESCENDING
    else:
        s = sort, SortDirection.ASCENDING

    if not hasattr(document, s[0]):
        raise InvalidSortError(s)

    return s
