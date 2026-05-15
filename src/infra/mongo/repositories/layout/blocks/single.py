from typing import TYPE_CHECKING

from .base import LayoutBlockRepository

if TYPE_CHECKING:
    from src.domain.annotations import (
        LayoutSingleCursorFiltersType,
        LayoutSingleLimitOffsetFiltersType,
        LayoutSinglePageFiltersType,
    )
    from src.domain.models.entities import BaseEntity
    from src.domain.models.pagination import (
        CursorResult,
        LimitOffsetResult,
        PagesResult,
    )
    from src.domain.protocols.pagination import (
        LayoutBlockSingleFiltersProtocol,
    )
    from src.infra.mongo.annotations import QueryConditionsType


class LayoutBlockSingleRepository(LayoutBlockRepository):
    async def get_all_pages[R](
        self,
        filters: LayoutSinglePageFiltersType,
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
        filters: LayoutSingleLimitOffsetFiltersType,
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
        filters: LayoutSingleCursorFiltersType,
        *,
        return_as: type[R],
    ) -> CursorResult[R] | None:
        return await self._get_all_cursor(
            conditions=self._pagination_conditions(filters),
            params=filters.pagination_params,
            return_as=return_as,
        )

    def _pagination_conditions(
        self, filters: LayoutBlockSingleFiltersProtocol
    ) -> QueryConditionsType:
        conditions = []

        return conditions  # noqa: RET504
