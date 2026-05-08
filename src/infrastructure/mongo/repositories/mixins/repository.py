from collections.abc import Iterable, MutableMapping, Sequence
from typing import TYPE_CHECKING, Any

from beanie import BackLink, Link, PydanticObjectId
from bson.errors import InvalidId

from src.domain.constants import CURSOR_SEPARATOR
from src.infrastructure.mongo.errors import InvalidMongoIDError

if TYPE_CHECKING:
    from beanie import Document
    from pydantic import BaseModel
    from pymongo.asynchronous.client_session import AsyncClientSession
    from pymongo.asynchronous.collection import AsyncCollection


class BaseRepository:
    _session: AsyncClientSession | None

    def __init__[D: Document](self, document: type[D]) -> None:
        self._document = document
        self._session = None

    @property
    def collection(self) -> AsyncCollection:
        return self._document.get_pymongo_collection()

    def start_session(self) -> AsyncClientSession:
        return self.collection.database.client.start_session()

    def set_session(self, session: AsyncClientSession | None) -> None:
        self._session = session

    def as_ids(self, ids: Sequence[str], /) -> Sequence[PydanticObjectId]:
        return [self.as_id(i) for i in ids]

    @staticmethod
    def as_id(_id: str, /) -> PydanticObjectId:
        s = _id.split(CURSOR_SEPARATOR, 1)
        try:
            if len(s) == 1:
                return PydanticObjectId(_id)
            return PydanticObjectId(s[-1])
        except InvalidId as e:
            raise InvalidMongoIDError(_id) from e

    def as_dtos[D: BaseModel, R](
        self, docs: Iterable[D], dto: type[R], *, replace_links: bool = False
    ) -> list[R]:
        return [self.as_dto(d, dto, replace_links=replace_links) for d in docs]

    @staticmethod
    def as_dto[D: BaseModel, R](
        doc: D, dto: type[R], *, replace_links: bool = False
    ) -> R:
        dump = doc.model_dump()
        if replace_links:
            _link_replacer(dump)
        return dto(**dump)


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
            del dump[k]
    elif isinstance(dump, list):
        for i in dump:
            _link_replacer(i)
