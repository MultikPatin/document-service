from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING, Any

from .base import LayoutBlockRepository

if TYPE_CHECKING:
    from pymongo.asynchronous.client_session import AsyncClientSession

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
    from src.application.protocols.pagination import (
        LayoutBlockTablePaginationFiltersProtocol,
    )


class LayoutBlockTableRepository(LayoutBlockRepository):
    async def get_all_pages[R](
        self,
        filters: LayoutBlockTablePaginationFiltersProtocol[PagesParamsProtocol],
        *,
        session: AsyncClientSession,
        return_as: type[R],
    ) -> PagesResultDTO[R] | None:
        return await self._get_all_pages(
            conditions=self._pagination_conditions(filters),
            params=filters.pagination_params,
            session=session,
            return_as=return_as,
        )

    async def get_all_limit_offset[R](
        self,
        filters: LayoutBlockTablePaginationFiltersProtocol[
            LimitOffsetParamsProtocol
        ],
        *,
        session: AsyncClientSession,
        return_as: type[R],
    ) -> LimitOffsetResultDTO[R] | None:
        return await self._get_all_limit_offset(
            conditions=self._pagination_conditions(filters),
            session=session,
            params=filters.pagination_params,
            return_as=return_as,
        )

    async def get_all_cursor[R](
        self,
        filters: LayoutBlockTablePaginationFiltersProtocol[
            CursorParamsProtocol
        ],
        *,
        session: AsyncClientSession,
        return_as: type[R],
    ) -> CursorResultDTO[R] | None:
        return await self._get_all_cursor(
            conditions=self._pagination_conditions(filters),
            session=session,
            params=filters.pagination_params,
            return_as=return_as,
        )

    def _pagination_conditions(
        self, filters: LayoutBlockTablePaginationFiltersProtocol
    ) -> Sequence[Mapping[Any, Any] | bool]:
        conditions = []

        return conditions  # noqa: RET504
