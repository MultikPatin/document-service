from dataclasses import asdict
from typing import TYPE_CHECKING

from fastapi import FastAPI

from src.api.core.static_docs import register_static_docs

if TYPE_CHECKING:
    from src.api.core.contexts import MountBuilderContex, RouterContex


class MountBuilder:
    def __init__(self, ctx: MountBuilderContex) -> None:
        self._routers_ctx: list[RouterContex] = []
        self._ctx = ctx
        self._api = FastAPI(
            title=ctx.title,
            description=ctx.description,
            version=ctx.version,
            docs_url=ctx.docs_url,
            redoc_url=None,
        )

    @property
    def path(self) -> str:
        return self._ctx.path

    def build(self) -> FastAPI:
        self._register_static_docs()
        self._register_routers_ctx()
        return self._api

    def include_router_ctx(self, ctx: RouterContex) -> None:
        self._routers_ctx.append(ctx)

    def _register_routers_ctx(self) -> None:
        # TODO Raise Error if self._router_ctxs = []
        for rc in self._routers_ctx:
            self._api.include_router(**asdict(rc))

    def _register_static_docs(self) -> None:
        if self._ctx.use_static_docs:
            register_static_docs(app=self._api, path=self._ctx.static_docs_path)
