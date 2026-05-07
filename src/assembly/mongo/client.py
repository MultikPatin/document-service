import logging
from collections.abc import AsyncGenerator

from dishka import Provider, Scope, provide

from src.assembly import InitComponentProtocol
from src.infrastructure.mongo import Client, Settings, collect_documents
from src.infrastructure.mongo.logger import LoggerNames

logger = logging.getLogger(LoggerNames.init())


class ClientProvider(Provider):
    @provide(scope=Scope.APP)
    async def __init(self, client: Client) -> InitComponentProtocol:
        logger.info("component initialization completed successfully")
        return InitComponentProtocol

    @provide(scope=Scope.APP)
    async def __settings(self) -> Settings:
        logger.info("loading the settings...")
        settings = Settings()

        params = {
            "client_kwargs": settings.client_kwargs,
            "database": settings.database,
            "connection": settings.dsn().encoded_string(),
        }
        logger.debug("settings parameters: %s", params)

        logger.info("settings was loaded successfully")
        return settings

    @provide(scope=Scope.APP)
    async def __client(self, settings: Settings) -> AsyncGenerator[Client]:
        logger.info("component initialization...")
        logger.info("client initialization...")
        client = Client(settings)
        logger.info("client initialization completed successfully")

        logger.info("Collecting documents...")
        documents = collect_documents()
        logger.debug("Collect document: %s", [d.__name__ for d in documents])
        logger.info("Collecting documents completed successfully")

        logger.info("beanie initialization...")
        await client.init_beanie(documents)
        logger.info("beanie initialization completed successfully")

        yield client

        logger.info("stopping the client...")
        await client.close()
        logger.info("stopping the client has been completed successfully")

    # session_alias = alias(source=AsyncClientSession, provides=SessionProtocol)

    # @provide(scope=Scope.REQUEST)
    # async def __session(
    #     self, client: Client
    # ) -> AsyncGenerator[AsyncClientSession, None]:
    #     session = client.start_session()
    #     yield session
    #     await session.end_session()
