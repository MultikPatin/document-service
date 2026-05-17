from dataclasses import asdict
from typing import TYPE_CHECKING

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware

from src.api.core.middlewares import ProcessTimeMiddleware

if TYPE_CHECKING:
    from src.api.core.contexts import CoreBuilderContex

    from .mount import MountBuilder


class CoreBuilder:
    def __init__(self, ctx: CoreBuilderContex) -> None:
        self._mount_builders: list[MountBuilder] = []
        self._ctx = ctx
        self._api = FastAPI(
            lifespan=ctx.lifespan,
            docs_url=None,
            redoc_url=None,
            openapi_url=None,
            root_path=ctx.root_path,
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
            **asdict(self._ctx.cors_middleware_ctx()),
        )
        if self._ctx.is_dev_mode:
            self._api.add_middleware(
                ProcessTimeMiddleware,
                **asdict(self._ctx.process_time_middleware_ctx()),
            )
        if self._ctx.is_gzip_enabled:
            self._api.add_middleware(
                GZipMiddleware,
                **asdict(self._ctx.gzip_middleware_ctx()),
            )
