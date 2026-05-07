from dataclasses import asdict
from typing import TYPE_CHECKING

from beanie import init_beanie
from pymongo import AsyncMongoClient

from .contexts import ClientContex, InitBeanieContex

if TYPE_CHECKING:
    from pymongo.asynchronous.client_session import AsyncClientSession
    from pymongo.asynchronous.collection import AsyncCollection
    from pymongo.asynchronous.database import AsyncDatabase

    from .annotations import DocumentsType
    from .settings import Settings


class Client:
    def __init__(
        self, settings: Settings, *, ctx: ClientContex | None = None
    ) -> None:
        if ctx is None:
            ctx = ClientContex()

        self._database = settings.database
        self._client = AsyncMongoClient(
            host=settings.connection_string,
            **asdict(ctx),
            **settings.client_kwargs,
        )

    async def init_beanie(
        self, documents: DocumentsType, *, ctx: InitBeanieContex | None = None
    ) -> None:
        if ctx is None:
            ctx = InitBeanieContex()

        await init_beanie(
            database=self.database,
            document_models=documents,
            **asdict(ctx),
        )

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

    def collection(self, name: str, /) -> AsyncCollection:
        return self.database[name]

    @property
    async def collections(self) -> list[str]:
        return await self.database.list_collection_names()

    async def drop_database(self) -> None:
        await self._client.drop_database(self._database)

    async def drop_collection(self, name: str, /) -> None:
        collection = self.collection(name)
        await collection.drop()
