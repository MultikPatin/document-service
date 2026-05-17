from .blocks import router as blocks_router
from .report import router

__all__ = ["router"]


router.include_router(router=blocks_router, prefix="/blocks")
