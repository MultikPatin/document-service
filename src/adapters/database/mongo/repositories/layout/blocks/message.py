from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING, Any

from .base import _Repository

if TYPE_CHECKING:
    from libs.core.dtos.pagination import (
        CursorResultDTO,
        LimitOffsetResultDTO,
        PagesResultDTO,
    )
    from libs.core.protocols.pagination import (
        CursorParamsProtocol,
        LimitOffsetParamsProtocol,
        PagesParamsProtocol,
    )
    from pymongo.asynchronous.client_session import AsyncClientSession

    from src.application.protocols.layout.pagination import (
        LayoutBlockMessagePaginationFiltersProtocol,
    )

type Session = AsyncClientSession


class LayoutBlockMessageRepository(_Repository):
    async def get_all_pages[ReturnSchema](
        self,
        filters: LayoutBlockMessagePaginationFiltersProtocol[
            PagesParamsProtocol
        ],
        *,
        session: Session,
        return_as: type[ReturnSchema],
    ) -> PagesResultDTO[ReturnSchema] | None:
        conditions = self._pagination_conditions(filters)
        return await self._get_all_pages(
            conditions,
            params=filters.pagination_params,
            session=session,
            return_as=return_as,
        )

    async def get_all_limit_offset[ReturnSchema](
        self,
        filters: LayoutBlockMessagePaginationFiltersProtocol[
            LimitOffsetParamsProtocol
        ],
        *,
        session: Session,
        return_as: type[ReturnSchema],
    ) -> LimitOffsetResultDTO[ReturnSchema] | None:
        conditions = self._pagination_conditions(filters)
        return await self._get_all_limit_offset(
            conditions,
            params=filters.pagination_params,
            session=session,
            return_as=return_as,
        )

    async def get_all_cursor[ReturnSchema](
        self,
        filters: LayoutBlockMessagePaginationFiltersProtocol[
            CursorParamsProtocol
        ],
        *,
        session: Session,
        return_as: type[ReturnSchema],
    ) -> CursorResultDTO[ReturnSchema] | None:
        conditions = self._pagination_conditions(filters)
        return await self._get_all_cursor(
            conditions,
            params=filters.pagination_params,
            session=session,
            return_as=return_as,
        )

    def _pagination_conditions(
        self,
        filters: LayoutBlockMessagePaginationFiltersProtocol,
    ) -> Sequence[Mapping[Any, Any] | bool]:
        conditions = []

        return conditions  # noqa: RET504
