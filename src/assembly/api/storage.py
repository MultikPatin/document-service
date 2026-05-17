__all__ = ["create_app"]

import logging
from typing import TYPE_CHECKING

from dishka.integrations.fastapi import FastapiProvider, setup_dishka

from src.api.core.contexts import CoreContex
from src.api.core.settings.api import CoreSettings
from src.api.storage import make_app
from src.assembly.domain import make_container
from src.assembly.logger import LoggerNames

from .lifespan import lifespan

if TYPE_CHECKING:
    from fastapi import FastAPI

logger = logging.getLogger(LoggerNames.init())


def create_app() -> FastAPI:
    logger.info("loading api settings...")
    settings = CoreSettings()
    logger.info("api settings was loaded successfully")

    logger.info("start assembly application container...")
    container = make_container(FastapiProvider())
    logger.info("assembly of the application container completed successfully")

    logger.info("api initialization...")

    ctx = CoreContex(settings=settings, lifespan=lifespan)
    app = make_app(ctx)
    setup_dishka(container=container, app=app)

    logger.info("api initialization completed successfully")

    return app
