from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter

from .message import router as block_message
from .single import router as block_single
from .table import router as block_table

__all__ = ["router"]


router = APIRouter(route_class=DishkaRoute)

router.include_router(router=block_message, prefix="/messages")
router.include_router(router=block_single, prefix="/singles")
router.include_router(router=block_table, prefix="/tables")
