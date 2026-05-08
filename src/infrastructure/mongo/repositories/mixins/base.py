from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from beanie import Document
    from pymongo.asynchronous.client_session import AsyncClientSession
    from pymongo.asynchronous.collection import AsyncCollection

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
