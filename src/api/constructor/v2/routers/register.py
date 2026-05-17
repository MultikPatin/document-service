from typing import TYPE_CHECKING

from .layout import router as layout_router

if TYPE_CHECKING:
    from fastapi import FastAPI


def register_routers(app: FastAPI) -> None:
    app.include_router(router=layout_router, prefix="/layouts")
