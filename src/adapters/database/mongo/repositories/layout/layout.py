from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING, Any

from libs.mongo.mixins.repository_methods import (
    GetMixin,
    PaginationCursorMixin,
    PaginationLimitOffsetMixin,
    PaginationPagesMixin,
)
from src.domain.constants import LifeStatusEnum

from .projections import _PaginatedLayoutProjection

if TYPE_CHECKING:
    from pymongo.asynchronous.client_session import AsyncClientSession

    from src.application.protocols.pagination import (
        LayoutPaginationFiltersProtocol,
    )
    from src.domain.entities import BaseEntity
    from src.domain.models.pagination import (
        CursorResult,
        LimitOffsetResult,
        PagesResult,
    )
    from src.domain.protocols.pagination import (
        CursorParamsProtocol,
        LimitOffsetParamsProtocol,
        PagesParamsProtocol,
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
    ) -> PagesResult[R] | None:
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
    ) -> LimitOffsetResult[R] | None:
        return await self._get_all_limit_offset(
            conditions=self._pagination_conditions(filters),
            params=filters.pagination_params,
            session=session,
            return_as=return_as,
            projection=_PaginatedLayoutProjection,
        )

    async def get_all_cursor[R: BaseEntity](
        self,
        filters: LayoutPaginationFiltersProtocol[CursorParamsProtocol],
        *,
        session: AsyncClientSession,
        return_as: type[R],
    ) -> CursorResult[R] | None:
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
