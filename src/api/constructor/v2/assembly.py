from src.api.core.builders import MountBuilder
from src.api.core.contexts import (
    CoreBuilderContex,
    MountBuilderContex,
    RouterContex,
)

from .controllers.layout import router
from .settings import Settings


def make_mount_builder(
    settings: Settings, ctx: CoreBuilderContex
) -> MountBuilder:
    builder = MountBuilder(MountBuilderContex.from_core_ctx(settings, ctx))
    builder.include_router_ctx(
        RouterContex(
            router=router,
            prefix="/layouts",
        ),
    )
    return builder
