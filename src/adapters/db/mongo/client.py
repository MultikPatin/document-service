from typing import TYPE_CHECKING

from beanie import init_beanie
from pymongo import AsyncMongoClient

if TYPE_CHECKING:
    from pymongo.asynchronous.client_session import AsyncClientSession
    from pymongo.asynchronous.collection import AsyncCollection
    from pymongo.asynchronous.database import AsyncDatabase

    from .documents import DocumentsType
    from .settings import _Settings


class _Client:
    def __init__(self, settings: _Settings) -> None:
        self._database = settings.DATABASE
        self._client = AsyncMongoClient(
            settings.dsn.unicode_string(),
            tz_aware=settings.TIMEZONE_AWARE,
            **settings.get_client_kwargs(),
        )

    async def init(self, documents: DocumentsType) -> None:
        await init_beanie(database=self.database, document_models=documents)

    async def close(self) -> None:
        await self._client.aclose()

    def start_session(self) -> AsyncClientSession:
        return self._client.start_session()

    @property
    def client(self) -> AsyncMongoClient:
        return self._client

    @property
    def database(self) -> AsyncDatabase:
        return self._client[self._database]

    def collection(self, name: str) -> AsyncCollection:
        return self.database[name]

    @property
    async def collections(self) -> list[str]:
        return await self.database.list_collection_names()

    async def drop_database(self) -> None:
        await self._client.drop_database(self._database)

    async def drop_collection(self, name: str) -> None:
        collection = self.collection(name)
        await collection.drop()
