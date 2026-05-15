import logging

from dishka import AsyncContainer, Provider, Scope, from_context, provide
from dishka.integrations.fastapi import setup_dishka

from src.api import ApiBuilder, Settings
from src.assembly.logger import LoggerNames
from src.assembly.protocols import ApiBuilderProtocol

from .lifespan import lifespan

logger = logging.getLogger(LoggerNames.init())


class ApiProvider(Provider):
    container = from_context(provides=AsyncContainer, scope=Scope.APP)

    @provide(scope=Scope.APP)
    def __settings(self) -> Settings:
        logger.info("loading the api settings...")
        settings = Settings()
        logger.info("api settings was loaded successfully")
        return settings

    @provide(scope=Scope.APP)
    def __api(
        self, settings: Settings, container: AsyncContainer
    ) -> ApiBuilderProtocol:
        logger.info("api initialization...")
        builder = ApiBuilder(settings, lifespan)
        setup_dishka(container=container, app=builder.api)
        logger.info("api initialization completed successfully")
        return builder
