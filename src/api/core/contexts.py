from collections.abc import Callable, Sequence
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any

from fastapi.datastructures import Default
from fastapi.utils import generate_unique_id
from starlette.responses import JSONResponse

from .constants import API_HEADER_PROCESS_TIME
from .enums import URLEnum

if TYPE_CHECKING:
    from enum import Enum

    from fastapi import FastAPI
    from fastapi.params import Depends
    from fastapi.routing import APIRoute, APIRouter
    from starlette.responses import Response
    from starlette.routing import BaseRoute
    from starlette.types import Lifespan

    from .settings.api import CoreSettings, MountSettings


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
class CORSMiddlewareContex:
    allow_origins: list[str]
    allow_headers: list[str]
    allow_methods: list[str]


@dataclass(frozen=True, slots=True, eq=False, match_args=False, kw_only=True)
class GZipMiddlewareContex:
    minimum_size: int
    compresslevel: int


@dataclass(frozen=True, slots=True, eq=False, match_args=False, kw_only=True)
class ProcessTimeMiddlewareContex:
    header_name: str = field(default=API_HEADER_PROCESS_TIME)


@dataclass(frozen=True, slots=True, eq=False, match_args=False, kw_only=True)
class CoreBuilderContex:
    settings: CoreSettings
    lifespan: Lifespan[FastAPI] | None = None

    @property
    def is_dev_mode(self) -> bool:
        return self.settings.IS_DEV_MODE

    @property
    def is_gzip_enabled(self) -> bool:
        return self.settings.gzip.ENABLE

    @property
    def root_path(self) -> str:
        return self.settings.ROOT_PATH

    def cors_middleware_ctx(self) -> CORSMiddlewareContex:
        return CORSMiddlewareContex(
            allow_origins=self.settings.ALLOW_ORIGINS,
            allow_headers=self.settings.ALLOW_HEADERS,
            allow_methods=self.settings.ALLOW_METHODS,
        )

    def gzip_middleware_ctx(self) -> GZipMiddlewareContex:
        return GZipMiddlewareContex(
            minimum_size=self.settings.gzip.MIN_SIZE,
            compresslevel=self.settings.gzip.COMPRESS_LEVEL,
        )

    @staticmethod
    def process_time_middleware_ctx() -> ProcessTimeMiddlewareContex:
        return ProcessTimeMiddlewareContex()


@dataclass(frozen=True, slots=True, eq=False, match_args=False, kw_only=True)
class MountBuilderContex:
    settings: MountSettings
    is_dev_mode: bool
    root_path: str

    @classmethod
    def from_core_ctx(
        cls, settings: MountSettings, ctx: CoreBuilderContex
    ) -> MountBuilderContex:
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
