from dataclasses import dataclass
from typing import TYPE_CHECKING

from src.api.core.enums import URLEnum

if TYPE_CHECKING:
    from starlette.types import ASGIApp

    from src.api.core.settings.api import MountSettings

    from .core import CoreContex


@dataclass(frozen=True, slots=True, eq=False, match_args=False)
class MountableAppContex:
    app: ASGIApp
    path: str
    name: str | None = None


@dataclass(frozen=True, slots=True, eq=False, match_args=False, kw_only=True)
class MountableContex:
    settings: MountSettings
    is_dev_mode: bool
    root_path: str

    @classmethod
    def from_core_ctx(
        cls, settings: MountSettings, ctx: CoreContex
    ) -> MountableContex:
        return cls(
            settings=settings,
            is_dev_mode=ctx.is_dev_mode,
            root_path=ctx.root_path,
        )

    @property
    def path(self) -> str:
        return f"/v{self.settings.VERSION}"

    @property
    def version(self) -> str:
        return str(self.settings.VERSION)

    @property
    def title(self) -> str:
        return self.settings.TITLE

    @property
    def description(self) -> str:
        return self.settings.DESCRIPTION

    @property
    def use_static_docs(self) -> bool:
        return self.settings.IS_STATIC_DOCS or not self.is_dev_mode

    @property
    def static_docs_path(self) -> str:
        return self.root_path + self.path

    @property
    def docs_url(self) -> str | None:
        return None if self.use_static_docs else URLEnum.docs
