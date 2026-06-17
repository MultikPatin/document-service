from collections.abc import Iterable, MutableMapping, Sequence
from typing import TYPE_CHECKING, Any

from beanie import BackLink, Link, PydanticObjectId
from bson.errors import InvalidId

from src.domain.constants import CURSOR_SEPARATOR
from src.infra.mongo.errors import InvalidIDError

if TYPE_CHECKING:
    from pydantic import BaseModel


class Converter:
    @staticmethod
    def as_id(id_: str) -> PydanticObjectId:
        s = id_.split(CURSOR_SEPARATOR, 1)
        try:
            if len(s) == 1:
                return PydanticObjectId(id_)
            return PydanticObjectId(s[-1])
        except InvalidId as e:
            raise InvalidIDError(id_) from e

    def as_ids(self, ids: Iterable[str]) -> Iterable[PydanticObjectId]:
        return [self.as_id(i) for i in ids]

    @staticmethod
    def as_dto[D: BaseModel, R](
        document: D, return_as: type[R], *, replace_links: bool = False
    ) -> R:
        dump = document.model_dump()
        if replace_links:
            _link_replacer(dump)
        return return_as(**dump)

    def as_dtos[D: BaseModel, R](
        self,
        documents: Iterable[D],
        return_as: type[R],
        *,
        replace_links: bool = False,
    ) -> list[R]:
        return [
            self.as_dto(d, return_as, replace_links=replace_links)
            for d in documents
        ]


def _link_replacer(dump: MutableMapping[str, Any] | Sequence[Any]) -> None:
    if isinstance(dump, dict):
        to_delete = []
        for k in dump:
            if isinstance(dump[k], Link):  # ty:ignore[invalid-argument-type]
                dump[k] = str(dump[k].ref.id)  # ty:ignore[invalid-assignment, invalid-argument-type]
            elif isinstance(dump[k], BackLink):  # ty:ignore[invalid-argument-type]
                to_delete.append(k)
            else:
                _link_replacer(dump[k])  # ty:ignore[invalid-argument-type]
        for k in to_delete:
            del dump[k]  # ty:ignore[not-subscriptable]
    elif isinstance(dump, list):
        for i in dump:
            _link_replacer(i)
