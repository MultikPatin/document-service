from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from beanie import Document
    from pymongo.asynchronous.client_session import AsyncClientSession


class BaseInteractor[D: Document]:
    __slots__ = ("_document", "_session")

    def __init__(
        self, document: type[D], session: AsyncClientSession | None = None
    ) -> None:
        self._document = document
        self._session = session
