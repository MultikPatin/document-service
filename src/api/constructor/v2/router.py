from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter

from .controllers.layout.blocks.message import router as block_message
from .controllers.layout.blocks.single import router as block_single
from .controllers.layout.blocks.table import router as block_table
from .controllers.layout.layers.default import router as layer_default
from .controllers.layout.layers.schema import router as layer_schema
from .controllers.layout.layers.validation import router as layer_validation
from .controllers.layout.layout import router as layout_router

__all__ = ["router"]


blocks_router = APIRouter(route_class=DishkaRoute)

blocks_router.include_router(router=block_message, prefix="/messages")
blocks_router.include_router(router=block_single, prefix="/singles")
blocks_router.include_router(router=block_table, prefix="/tables")

layers_router = APIRouter(route_class=DishkaRoute)

layers_router.include_router(router=layer_schema, prefix="/schemas")
layers_router.include_router(router=layer_validation, prefix="/validations")
layers_router.include_router(router=layer_default, prefix="/defaults")

layout_router.include_router(router=blocks_router, prefix="/blocks")
layout_router.include_router(router=layers_router, prefix="/layers")

router = APIRouter(route_class=DishkaRoute)

router.include_router(router=layout_router, prefix="/layouts")
