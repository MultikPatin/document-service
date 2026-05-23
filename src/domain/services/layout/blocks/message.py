from typing import TYPE_CHECKING

from src.domain.models.entities import LayoutBlockMessageEntity

if TYPE_CHECKING:
    from src.domain.annotations import (
        LayoutMessageCursorFiltersType,
        LayoutMessageLimitOffsetFiltersType,
        LayoutMessagePageFiltersType,
    )
    from src.domain.models.pagination import (
        CursorResult,
        LimitOffsetResult,
        PagesResult,
    )
    from src.domain.protocols.repositories import (
        LayoutBlockMessageRepositoryProtocol,
    )


class LayoutBlockMessageService:
    def __init__(self, repo: LayoutBlockMessageRepositoryProtocol) -> None:
        self._repo = repo

    async def get(self, id_: str) -> LayoutBlockMessageEntity | None:
        return await self._repo.get(id_)

    async def get_all_pages(
        self, filters: LayoutMessagePageFiltersType
    ) -> PagesResult[LayoutBlockMessageEntity] | None:
        return await self._repo.get_all_pages(
            filters, projection=LayoutBlockMessageEntity
        )

    async def get_all_limit_offset(
        self, filters: LayoutMessageLimitOffsetFiltersType
    ) -> LimitOffsetResult[LayoutBlockMessageEntity] | None:
        return await self._repo.get_all_limit_offset(
            filters, projection=LayoutBlockMessageEntity
        )

    async def get_all_cursor(
        self, filters: LayoutMessageCursorFiltersType
    ) -> CursorResult[LayoutBlockMessageEntity] | None:
        return await self._repo.get_all_cursor(
            filters, projection=LayoutBlockMessageEntity
        )
