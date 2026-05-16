from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter

from .controllers.layout.layout import router as layout_router
from .controllers.report.blocks.single import router as block_single
from .controllers.report.blocks.table import router as block_table
from .controllers.report.report import router as report_router

__all__ = ["router"]

blocks_router = APIRouter(route_class=DishkaRoute)

blocks_router.include_router(router=block_single, prefix="/singles")
blocks_router.include_router(router=block_table, prefix="/tables")

report_router.include_router(router=blocks_router, prefix="/blocks")

router = APIRouter(route_class=DishkaRoute)

router.include_router(router=layout_router, prefix="/layouts")
router.include_router(router=report_router, prefix="/reports")
