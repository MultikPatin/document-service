from typing import TYPE_CHECKING

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from starlette.types import Lifespan

from .constants import API_HEADER_PROCESS_TIME
from .enums import URLEnum
from .middlewares import ProcessTimeHeaderMiddleware
from .static_docs import register_static_docs

if TYPE_CHECKING:
    from .settings import Settings


class ApiBuilder:
    def __init__(
        self, settings: Settings, lifespan: Lifespan[FastAPI] | None = None
    ) -> None:
        self._settings = settings
        self._api = FastAPI(
            lifespan=lifespan,
            docs_url=self._get_docs_url(),
            redoc_url=None,
            # openapi_url=None,
            root_path=settings.ROOT_PATH,
        )

    def _get_docs_url(self) -> str | None:
        return (
            None
            if self._settings.IS_STATIC_DOCS or not self._settings.IS_DEV_MODE
            else URLEnum.docs
        )

    @property
    def api(self) -> FastAPI:
        return self._api

    # def mount(self, app: "VAppProtocol") -> None:
    #     self._api.mount(path=app.path, app=app.api)

    def build(self) -> FastAPI:
        self._register_middlewares()
        self._register_static_docs()
        return self._api

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

    def _register_static_docs(self) -> None:
        if self._settings.IS_STATIC_DOCS and self._settings.IS_DEV_MODE:
            register_static_docs(app=self._api, path=self._settings.ROOT_PATH)
