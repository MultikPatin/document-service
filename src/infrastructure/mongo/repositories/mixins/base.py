from collections.abc import Iterable
from typing import TYPE_CHECKING

from beanie.odm.enums import SortDirection

from src.domain.constants import SORT_DESC_PREFIX
from src.infrastructure.mongo.errors import InvalidSortError

if TYPE_CHECKING:
    from beanie import Document
    from pymongo.asynchronous.client_session import AsyncClientSession
    from pymongo.asynchronous.collection import AsyncCollection

    from src.infrastructure.mongo.annotations import QuerySortType
    from src.infrastructure.mongo.protocols import ConverterProtocol


class BaseRepository:
    _session: AsyncClientSession | None

    def __init__[D: Document](
        self, document: type[D], *, converter: ConverterProtocol
    ) -> None:
        self._session = None
        self._document = document
        self.converter = converter

    @property
    def collection(self) -> AsyncCollection:
        return self._document.get_pymongo_collection()

    def start_session(self) -> AsyncClientSession:
        return self.collection.database.client.start_session()

    def set_session(self, session: AsyncClientSession | None) -> None:
        self._session = session

    def prepare_sort(self, sort: str | Iterable[str] | None) -> QuerySortType:
        if sort is None:
            return None
        if isinstance(sort, str):
            return [self._split_sort(sort)]
        if isinstance(sort, Iterable):
            return [self._split_sort(s) for s in sort]
        raise InvalidSortError(sort)

    def _split_sort(self, sort: str) -> tuple[str, SortDirection]:
        if sort.startswith(SORT_DESC_PREFIX):
            s = sort.removeprefix(SORT_DESC_PREFIX), SortDirection.DESCENDING
        else:
            s = sort, SortDirection.ASCENDING

        if not hasattr(self._document, s[0]):
            raise InvalidSortError(s)

        return s
