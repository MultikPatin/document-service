from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from beanie import Document
    from pymongo.asynchronous.client_session import AsyncClientSession
    from pymongo.asynchronous.collection import AsyncCollection


class BaseRepository[D: Document]:
    _document: type[D]
    _session: AsyncClientSession | None

    def __init__(self) -> None:
        self._session = None

    @property
    def collection(self) -> AsyncCollection:
        return self._document.get_pymongo_collection()

    def start_session(self) -> AsyncClientSession:
        return self.collection.database.client.start_session()

    def set_session(self, session: AsyncClientSession | None) -> None:
        self._session = session
