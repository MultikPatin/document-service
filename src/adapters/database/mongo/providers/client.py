import logging
from collections.abc import AsyncGenerator

from dishka import Provider, Scope, provide

from libs.core.protocols import InitComponentProtocol
from libs.mongo.client import Client
from libs.mongo.constants.logger import LoggerNames
from src.adapters.database.mongo.documents import collect_documents
from src.adapters.database.mongo.settings import Settings

init_logger = logging.getLogger(LoggerNames.init())


class ClientProvider(Provider):
    @provide(scope=Scope.APP)
    async def __init(self, client: Client) -> InitComponentProtocol:
        return InitComponentProtocol

    @provide(scope=Scope.APP)
    async def __settings(self) -> Settings:
        return Settings(logger=init_logger)

    @provide(scope=Scope.APP)
    async def __client(self, settings: Settings) -> AsyncGenerator[Client]:
        client = Client(settings, init_logger)
        documents = collect_documents(init_logger)
        await client.init_beanie(documents)
        yield client
        await client.close()

    # session_alias = alias(source=AsyncClientSession, provides=SessionProtocol)

    # @provide(scope=Scope.REQUEST)
    # async def __session(
    #     self, client: Client
    # ) -> AsyncGenerator[AsyncClientSession, None]:
    #     session = client.start_session()
    #     yield session
    #     await session.end_session()
