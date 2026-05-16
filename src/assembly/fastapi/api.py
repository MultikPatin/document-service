import logging
from typing import TYPE_CHECKING

from dishka.integrations.fastapi import FastapiProvider, setup_dishka

from src.api import Builder, Settings
from src.api.constructor import v2 as constructor_pkg
from src.api.storage import v3 as storage_pkg
from src.assembly.app import make_container
from src.assembly.logger import LoggerNames

from .lifespan import lifespan

if TYPE_CHECKING:
    from fastapi import FastAPI

logger = logging.getLogger(LoggerNames.init())


def create_api() -> FastAPI:
    logger.info("loading api settings...")
    settings = Settings()
    logger.info("api settings was loaded successfully")

    logger.info("start assembly application container...")
    container = make_container(FastapiProvider())
    logger.info("assembly of the application container completed successfully")

    logger.info("api initialization...")
    builder = Builder(settings, lifespan)
    setup_dishka(container=container, app=builder.api)

    constructor = constructor_pkg.Builder(
        settings.IS_DEV_MODE,
        constructor_pkg.Settings(),
    )
    storage = storage_pkg.Builder(
        settings.IS_DEV_MODE,
        storage_pkg.Settings(),
    )

    builder.mount(
        app=constructor.build(settings.ROOT_PATH),
        path=constructor.path,
    )
    builder.mount(
        app=storage.build(settings.ROOT_PATH),
        path=storage.path,
    )

    logger.info("api initialization completed successfully")

    return builder.build()
