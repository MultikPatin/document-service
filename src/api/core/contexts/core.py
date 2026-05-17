from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from src.api.core.constants import API_HEADER_PROCESS_TIME
from src.api.core.settings.api import CoreSettings

if TYPE_CHECKING:
    from fastapi import FastAPI
    from starlette.types import Lifespan


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
class CoreContex:
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
