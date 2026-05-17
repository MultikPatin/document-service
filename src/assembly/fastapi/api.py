import logging
from typing import TYPE_CHECKING

from dishka.integrations.fastapi import FastapiProvider, setup_dishka

from src.api.constructor import v2
from src.api.core.builders import CoreBuilder
from src.api.core.contexts import CoreBuilderContex
from src.api.core.settings.api import CoreSettings
from src.api.storage import v3
from src.assembly.app import make_container
from src.assembly.logger import LoggerNames

from .lifespan import lifespan

if TYPE_CHECKING:
    from fastapi import FastAPI

logger = logging.getLogger(LoggerNames.init())


def create_api() -> FastAPI:
    logger.info("loading api settings...")
    settings = CoreSettings()
    logger.info("api settings was loaded successfully")

    logger.info("start assembly application container...")
    container = make_container(FastapiProvider())
    logger.info("assembly of the application container completed successfully")

    logger.info("api initialization...")

    ctx = CoreBuilderContex(
        settings=settings,
        lifespan=lifespan,
    )

    builder = CoreBuilder(ctx)
    setup_dishka(container=container, app=builder.api)

    builder.include_mount_builder(v2.make_mount_builder(v2.Settings(), ctx))
    builder.include_mount_builder(v3.make_mount_builder(v3.Settings(), ctx))

    logger.info("api initialization completed successfully")

    return builder.build()
