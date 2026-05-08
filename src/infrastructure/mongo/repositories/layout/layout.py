from typing import TYPE_CHECKING

from src.domain.enums import LifeStatusEnum
from src.infrastructure.mongo.projections import PaginatedLayoutProjection
from src.infrastructure.mongo.repositories.mixins import (
    GetMixin,
    PaginationCursorMixin,
    PaginationLimitOffsetMixin,
    PaginationPagesMixin,
)

if TYPE_CHECKING:
    from src.domain.annotations import (
        LayoutCursorFiltersType,
        LayoutLimitOffsetFiltersType,
        LayoutPageFiltersType,
    )
    from src.domain.models.entities import BaseEntity
    from src.domain.models.pagination import (
        CursorResult,
        LimitOffsetResult,
        PagesResult,
    )
    from src.domain.protocols.pagination import LayoutFiltersProtocol
    from src.infrastructure.mongo.annotations import QueryConditionsType


class LayoutRepository(
    GetMixin,
    PaginationCursorMixin,
    PaginationLimitOffsetMixin,
    PaginationPagesMixin,
):
    async def get_all_pages[R](
        self,
        filters: LayoutPageFiltersType,
        *,
        return_as: type[R],
    ) -> PagesResult[R] | None:
        return await self._get_all_pages(
            conditions=self._pagination_conditions(filters),
            params=filters.pagination_params,
            return_as=return_as,
            projection=PaginatedLayoutProjection,
        )

    async def get_all_limit_offset[R](
        self,
        filters: LayoutLimitOffsetFiltersType,
        *,
        return_as: type[R],
    ) -> LimitOffsetResult[R] | None:
        return await self._get_all_limit_offset(
            conditions=self._pagination_conditions(filters),
            params=filters.pagination_params,
            return_as=return_as,
            projection=PaginatedLayoutProjection,
        )

    async def get_all_cursor[R: BaseEntity](
        self,
        filters: LayoutCursorFiltersType,
        *,
        return_as: type[R],
    ) -> CursorResult[R] | None:
        return await self._get_all_cursor(
            conditions=self._pagination_conditions(filters),
            params=filters.pagination_params,
            return_as=return_as,
            projection=PaginatedLayoutProjection,
        )

    def _pagination_conditions(
        self, filters: LayoutFiltersProtocol
    ) -> QueryConditionsType:
        conditions = []

        if filters.status:
            conditions.append(self._document.status == filters.status)
        else:
            conditions.append(self._document.status == LifeStatusEnum.published)

        return conditions
