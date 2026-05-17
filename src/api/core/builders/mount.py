from dataclasses import asdict
from typing import TYPE_CHECKING

from fastapi import FastAPI

from src.api.core.contexts import IncludedRouterContex
from src.api.core.enums import URLEnum
from src.api.core.static_docs import register_static_docs

if TYPE_CHECKING:
    from src.api.core.settings.api_mounted import Settings


class Builder:
    def __init__[R: IncludedRouterContex, S: Settings](
        self, router_ctx: R, settings: S, *, is_dev_mode: bool
    ) -> None:
        self._settings = settings
        self._is_dev_mode = is_dev_mode
        self._path = settings.path

        self._api = FastAPI(
            title=settings.TITLE,
            description=settings.DESCRIPTION,
            version=str(settings.VERSION),
            docs_url=self._get_docs_url(),
        )

        self._api.include_router(**asdict(router_ctx))

    @property
    def path(self) -> str:
        return self._path

    def _get_docs_url(self) -> str | None:
        return (
            None
            if self._settings.IS_STATIC_DOCS or not self._is_dev_mode
            else URLEnum.docs
        )

    def build(self, root_path: str) -> FastAPI:
        self._register_static_docs(root_path)
        return self._api

    def _register_static_docs(self, root_path: str) -> None:
        if self._settings.IS_STATIC_DOCS and self._is_dev_mode:
            register_static_docs(app=self._api, path=root_path + self._path)
