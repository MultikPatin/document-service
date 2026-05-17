from collections.abc import Callable, Sequence
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any

from fastapi.datastructures import Default
from fastapi.utils import generate_unique_id
from starlette.responses import JSONResponse

if TYPE_CHECKING:
    from enum import Enum

    from fastapi.params import Depends
    from fastapi.routing import APIRoute, APIRouter
    from starlette.responses import Response
    from starlette.routing import BaseRoute


@dataclass(frozen=True, slots=True, eq=False, match_args=False)
class IncludedRouterContex:
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
