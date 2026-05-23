from typing import TYPE_CHECKING

from src.domain.models.entities import LayoutBlockTableEntity

if TYPE_CHECKING:
    from src.domain.annotations import (
        LayoutTableCursorFiltersType,
        LayoutTableLimitOffsetFiltersType,
        LayoutTablePageFiltersType,
    )
    from src.domain.models.pagination import (
        CursorResult,
        LimitOffsetResult,
        PagesResult,
    )
    from src.domain.protocols.repositories import (
        LayoutBlockTableRepositoryProtocol,
    )


class LayoutBlockTableService:
    def __init__(self, repo: LayoutBlockTableRepositoryProtocol) -> None:
        self._repo = repo

    async def get(self, id_: str) -> LayoutBlockTableEntity | None:
        return await self._repo.get(id_)

    async def get_all_pages(
        self, filters: LayoutTablePageFiltersType
    ) -> PagesResult[LayoutBlockTableEntity] | None:
        return await self._repo.get_all_pages(
            filters, projection=LayoutBlockTableEntity
        )

    async def get_all_limit_offset(
        self, filters: LayoutTableLimitOffsetFiltersType
    ) -> LimitOffsetResult[LayoutBlockTableEntity] | None:
        return await self._repo.get_all_limit_offset(
            filters, projection=LayoutBlockTableEntity
        )

    async def get_all_cursor(
        self, filters: LayoutTableCursorFiltersType
    ) -> CursorResult[LayoutBlockTableEntity] | None:
        return await self._repo.get_all_cursor(
            filters, projection=LayoutBlockTableEntity
        )
