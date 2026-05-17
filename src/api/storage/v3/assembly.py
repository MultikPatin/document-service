from src.api.core.builders import MountBuilder
from src.api.core.contexts import (
    CoreBuilderContex,
    MountBuilderContex,
    RouterContex,
)

from .controllers.layout import router as layout_router
from .controllers.report import router as report_router
from .settings import Settings


def make_mount_builder(
    settings: Settings, ctx: CoreBuilderContex
) -> MountBuilder:
    builder = MountBuilder(MountBuilderContex.from_core_ctx(settings, ctx))
    builder.include_router_ctx(
        RouterContex(
            router=layout_router,
            prefix="/layouts",
        ),
    )
    builder.include_router_ctx(
        RouterContex(
            router=report_router,
            prefix="/reports",
        ),
    )
    return builder
