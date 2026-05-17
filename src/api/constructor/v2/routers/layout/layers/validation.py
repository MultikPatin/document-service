from dishka.integrations.fastapi import DishkaRoute
from fastapi import APIRouter

router = APIRouter(route_class=DishkaRoute)


@router.post(
    "/",
    summary="Test endpoint",
)
async def get_all_pages() -> int:
    return 3
