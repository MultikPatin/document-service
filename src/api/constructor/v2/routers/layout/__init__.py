from .blocks import router as blocks_router
from .layers import router as layers_router
from .layout import router

__all__ = ["router"]

router.include_router(router=blocks_router, prefix="/blocks")
router.include_router(router=layers_router, prefix="/layers")
