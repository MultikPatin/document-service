from typing import TYPE_CHECKING

from .base import LayoutBlockRepository

if TYPE_CHECKING:
    from src.domain.annotations import (
        LayoutTableCursorFiltersType,
        LayoutTableLimitOffsetFiltersType,
        LayoutTablePageFiltersType,
    )
    from src.domain.models.entities import BaseEntity
    from src.domain.models.pagination import (
        CursorResult,
        LimitOffsetResult,
        PagesResult,
    )
    from src.domain.protocols.pagination import (
        LayoutBlockTableFiltersProtocol,
    )
    from src.infrastructure.mongo.annotations import QueryConditionsType


class LayoutBlockTableRepository(LayoutBlockRepository):
    async def get_all_pages[R](
        self,
        filters: LayoutTablePageFiltersType,
        *,
        return_as: type[R],
    ) -> PagesResult[R] | None:
        return await self._get_all_pages(
            conditions=self._pagination_conditions(filters),
            params=filters.pagination_params,
            return_as=return_as,
        )

    async def get_all_limit_offset[R](
        self,
        filters: LayoutTableLimitOffsetFiltersType,
        *,
        return_as: type[R],
    ) -> LimitOffsetResult[R] | None:
        return await self._get_all_limit_offset(
            conditions=self._pagination_conditions(filters),
            params=filters.pagination_params,
            return_as=return_as,
        )

    async def get_all_cursor[R: BaseEntity](
        self,
        filters: LayoutTableCursorFiltersType,
        *,
        return_as: type[R],
    ) -> CursorResult[R] | None:
        return await self._get_all_cursor(
            conditions=self._pagination_conditions(filters),
            params=filters.pagination_params,
            return_as=return_as,
        )

    def _pagination_conditions(
        self, filters: LayoutBlockTableFiltersProtocol
    ) -> QueryConditionsType:
        conditions = []

        return conditions  # noqa: RET504
