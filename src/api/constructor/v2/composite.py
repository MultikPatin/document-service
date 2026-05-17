from typing import TYPE_CHECKING

from fastapi import FastAPI

from src.api.core.contexts import MountableAppContex
from src.api.core.static_docs import register_static_docs

from .routers import register_routers

if TYPE_CHECKING:
    from src.api.core.contexts import MountableContex


def make_mountable_app_ctx(ctx: MountableContex) -> MountableAppContex:
    app = FastAPI(
        title=ctx.title,
        description=ctx.description,
        version=ctx.version,
        docs_url=ctx.docs_url,
        redoc_url=None,
    )

    register_routers(app)

    if ctx.use_static_docs:
        register_static_docs(app=app, path=ctx.static_docs_path)

    return MountableAppContex(app=app, path=ctx.path)
