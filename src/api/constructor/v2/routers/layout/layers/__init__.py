from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter

from .default import router as layer_default
from .schema import router as layer_schema
from .validation import router as layer_validation

__all__ = ["router"]


router = APIRouter(route_class=DishkaRoute)

router.include_router(router=layer_schema, prefix="/schemas")
router.include_router(router=layer_validation, prefix="/validations")
router.include_router(router=layer_default, prefix="/defaults")
