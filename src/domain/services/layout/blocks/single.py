from typing import TYPE_CHECKING

from src.domain.models.entities import LayoutBlockSingleEntity

if TYPE_CHECKING:
    from src.domain.annotations import (
        LayoutSingleCursorFiltersType,
        LayoutSingleLimitOffsetFiltersType,
        LayoutSinglePageFiltersType,
    )
    from src.domain.models.pagination import (
        CursorResult,
        LimitOffsetResult,
        PagesResult,
    )
    from src.domain.protocols.repositories import (
        LayoutBlockSingleRepositoryProtocol,
    )


class LayoutBlockSingleService:
    def __init__(self, repo: LayoutBlockSingleRepositoryProtocol) -> None:
        self._repo = repo

    async def get(self, id_: str) -> LayoutBlockSingleEntity | None:
        return await self._repo.get(id_)

    async def get_all_pages(
        self, filters: LayoutSinglePageFiltersType
    ) -> PagesResult[LayoutBlockSingleEntity] | None:
        return await self._repo.get_all_pages(
            filters, projection=LayoutBlockSingleEntity
        )

    async def get_all_limit_offset(
        self, filters: LayoutSingleLimitOffsetFiltersType
    ) -> LimitOffsetResult[LayoutBlockSingleEntity] | None:
        return await self._repo.get_all_limit_offset(
            filters, projection=LayoutBlockSingleEntity
        )

    async def get_all_cursor(
        self, filters: LayoutSingleCursorFiltersType
    ) -> CursorResult[LayoutBlockSingleEntity] | None:
        return await self._repo.get_all_cursor(
            filters, projection=LayoutBlockSingleEntity
        )
