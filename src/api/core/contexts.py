from collections.abc import Callable, Sequence
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any

from fastapi.datastructures import Default
from fastapi.utils import generate_unique_id
from starlette.responses import JSONResponse

from .enums import URLEnum

if TYPE_CHECKING:
    from enum import Enum

    from fastapi.params import Depends
    from fastapi.routing import APIRoute, APIRouter
    from starlette.responses import Response
    from starlette.routing import BaseRoute

    from .settings.api import MountSettings


@dataclass(frozen=True, slots=True, eq=False, match_args=False)
class RouterContex:
    router: APIRouter
    prefix: str = ""
    tags: list[str | Enum] | None = None
    dependencies: Sequence[Depends] | None = None
    responses: dict[int | str, dict[str, Any]] | None = None
    deprecated: bool | None = None
    include_in_schema: bool = True
    default_response_class: type[Response] = field(
        default_factory=lambda: Default(JSONResponse)
    )
    callbacks: list[BaseRoute] | None = None
    generate_unique_id_function: Callable[[APIRoute], str] = field(
        default_factory=lambda: Default(generate_unique_id)
    )


@dataclass(frozen=True, slots=True, eq=False, match_args=False, kw_only=True)
class MountBuilderContex:
    settings: MountSettings
    is_dev_mode: bool
    root_path: str

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
