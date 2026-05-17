from dataclasses import asdict
from typing import TYPE_CHECKING

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware

from src.api.core.contexts import MountableContex
from src.api.core.middlewares import ProcessTimeMiddleware
from src.api.storage import v3

if TYPE_CHECKING:
    from src.api.core.contexts import CoreContex, MountableAppContex


def _mountable_v3(ctx: CoreContex) -> MountableAppContex:
    return v3.make_mountable_app_ctx(
        MountableContex.from_core_ctx(v3.Settings(), ctx)
    )


def _mountable_ctxs(ctx: CoreContex) -> tuple[MountableAppContex]:
    return (_mountable_v3(ctx),)


def make_app(ctx: CoreContex) -> FastAPI:
    app = FastAPI(
        lifespan=ctx.lifespan,
        docs_url=None,
        redoc_url=None,
        openapi_url=None,
        root_path=ctx.root_path,
    )

    for c in _mountable_ctxs(ctx):
        app.mount(app=c.app, path=c.path)

    app.add_middleware(
        CORSMiddleware,
        **asdict(ctx.cors_middleware_ctx()),
    )
    if ctx.is_dev_mode:
        app.add_middleware(
            ProcessTimeMiddleware,
            **asdict(ctx.process_time_middleware_ctx()),
        )
    if ctx.is_gzip_enabled:
        app.add_middleware(
            GZipMiddleware,
            **asdict(ctx.gzip_middleware_ctx()),
        )

    return app
