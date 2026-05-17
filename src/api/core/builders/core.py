from typing import TYPE_CHECKING

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware

from src.api.core.constants import API_HEADER_PROCESS_TIME
from src.api.core.middlewares import ProcessTimeHeaderMiddleware

if TYPE_CHECKING:
    from starlette.types import Lifespan

    from src.api.core.settings.api import CoreSettings

    from .mount import MountBuilder


class CoreBuilder:
    def __init__[S: CoreSettings](
        self, settings: S, *, lifespan: Lifespan[FastAPI] | None = None
    ) -> None:
        self._mount_builders: list[MountBuilder] = []
        self._settings = settings
        self._api = FastAPI(
            lifespan=lifespan,
            docs_url=None,
            redoc_url=None,
            openapi_url=None,
            root_path=settings.ROOT_PATH,
        )

    @property
    def api(self) -> FastAPI:
        return self._api

    def build(self) -> FastAPI:
        self._register_middlewares()
        self._register_mount_builders()
        return self._api

    def include_mount_builder(self, builder: MountBuilder) -> None:
        self._mount_builders.append(builder)

    def _register_mount_builders(self) -> None:
        # TODO Raise Error if self._mount_builders = []
        for mb in self._mount_builders:
            self._api.mount(app=mb.build(), path=mb.path)

    def _register_middlewares(self) -> None:
        self._api.add_middleware(
            CORSMiddleware,
            allow_origins=self._settings.ALLOW_ORIGINS,
            allow_headers=self._settings.ALLOW_HEADERS,
            allow_methods=self._settings.ALLOW_METHODS,
        )
        if self._settings.IS_DEV_MODE:
            self._api.add_middleware(
                ProcessTimeHeaderMiddleware,
                header_name=API_HEADER_PROCESS_TIME,
            )
        if self._settings.gzip.ENABLE:
            self._api.add_middleware(
                GZipMiddleware,
                minimum_size=self._settings.gzip.MIN_SIZE,
                compresslevel=self._settings.gzip.COMPRESS_LEVEL,
            )
