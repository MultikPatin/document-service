from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING, Any

from libs.core.enums import LifeStatusEnum
from libs.mongo.mixins.repository_methods import (
    GetMixin,
    PaginationCursorMixin,
    PaginationLimitOffsetMixin,
    PaginationPagesMixin,
)

from .projections import _PaginatedLayoutProjection

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
        LayoutPaginationFiltersProtocol,
    )


class LayoutRepository(
    GetMixin,
    PaginationCursorMixin,
    PaginationLimitOffsetMixin,
    PaginationPagesMixin,
):
    async def get_all_pages[R](
        self,
        filters: LayoutPaginationFiltersProtocol[PagesParamsProtocol],
        *,
        session: AsyncClientSession,
        return_as: type[R],
    ) -> PagesResultDTO[R] | None:
        return await self._get_all_pages(
            conditions=self._pagination_conditions(filters),
            params=filters.pagination_params,
            session=session,
            return_as=return_as,
            projection=_PaginatedLayoutProjection,
        )

    async def get_all_limit_offset[R](
        self,
        filters: LayoutPaginationFiltersProtocol[LimitOffsetParamsProtocol],
        *,
        session: AsyncClientSession,
        return_as: type[R],
    ) -> LimitOffsetResultDTO[R] | None:
        return await self._get_all_limit_offset(
            conditions=self._pagination_conditions(filters),
            params=filters.pagination_params,
            session=session,
            return_as=return_as,
            projection=_PaginatedLayoutProjection,
        )

    async def get_all_cursor[R](
        self,
        filters: LayoutPaginationFiltersProtocol[CursorParamsProtocol],
        *,
        session: AsyncClientSession,
        return_as: type[R],
    ) -> CursorResultDTO[R] | None:
        return await self._get_all_cursor(
            conditions=self._pagination_conditions(filters),
            params=filters.pagination_params,
            session=session,
            return_as=return_as,
            projection=_PaginatedLayoutProjection,
        )

    def _pagination_conditions(
        self, filters: LayoutPaginationFiltersProtocol
    ) -> Sequence[Mapping[Any, Any] | bool]:
        conditions = []

        if filters.status:
            conditions.append(self._document.status == filters.status)
        else:
            conditions.append(self._document.status == LifeStatusEnum.published)

        return conditions
