from src.api.core.builders import MountBuilder
from src.api.core.contexts import MountBuilderContex, RouterContex

from .router import router
from .settings import Settings


def make_mount_builder(is_dev_mode: bool, root_path: str) -> MountBuilder:
    builder = MountBuilder(
        MountBuilderContex(
            settings=Settings(),
            is_dev_mode=is_dev_mode,
            root_path=root_path,
        ),
    )
    builder.include_router_ctx(
        RouterContex(
            router=router,
        ),
    )
    return builder
