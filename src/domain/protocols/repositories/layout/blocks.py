from typing import TYPE_CHECKING, Protocol

from src.domain.models.entities import (
    LayoutBlockMessageEntity,
    LayoutBlockSingleEntity,
    LayoutBlockTableEntity,
)

if TYPE_CHECKING:
    from pydantic import BaseModel

    from src.domain.annotations import (
        LayoutMessageCursorFiltersType,
        LayoutMessageLimitOffsetFiltersType,
        LayoutMessagePageFiltersType,
        LayoutSingleCursorFiltersType,
        LayoutSingleLimitOffsetFiltersType,
        LayoutSinglePageFiltersType,
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


class BlockRepositoryProtocol[E: BaseEntity](Protocol):
    async def get(self, id_: str) -> E | None: ...


class LayoutBlockSingleRepositoryProtocol(
    BlockRepositoryProtocol[LayoutBlockSingleEntity], Protocol
):
    async def get_all_pages[P: BaseModel](
        self, filters: LayoutSinglePageFiltersType, *, projection: type[P]
    ) -> PagesResult[P] | None: ...

    async def get_all_limit_offset[P: BaseModel](
        self,
        filters: LayoutSingleLimitOffsetFiltersType,
        *,
        projection: type[P],
    ) -> LimitOffsetResult[P] | None: ...

    async def get_all_cursor[P: BaseEntity](
        self, filters: LayoutSingleCursorFiltersType, *, projection: type[P]
    ) -> CursorResult[P] | None: ...


class LayoutBlockTableRepositoryProtocol(
    BlockRepositoryProtocol[LayoutBlockTableEntity], Protocol
):
    async def get_all_pages[P: BaseModel](
        self, filters: LayoutTablePageFiltersType, *, projection: type[P]
    ) -> PagesResult[P] | None: ...

    async def get_all_limit_offset[P: BaseModel](
        self,
        filters: LayoutTableLimitOffsetFiltersType,
        *,
        projection: type[P],
    ) -> LimitOffsetResult[P] | None: ...

    async def get_all_cursor[P: BaseEntity](
        self, filters: LayoutTableCursorFiltersType, *, projection: type[P]
    ) -> CursorResult[P] | None: ...


class LayoutBlockMessageRepositoryProtocol(
    BlockRepositoryProtocol[LayoutBlockMessageEntity], Protocol
):
    async def get_all_pages[P: BaseModel](
        self, filters: LayoutMessagePageFiltersType, *, projection: type[P]
    ) -> PagesResult[P] | None: ...

    async def get_all_limit_offset[P: BaseModel](
        self,
        filters: LayoutMessageLimitOffsetFiltersType,
        *,
        projection: type[P],
    ) -> LimitOffsetResult[P] | None: ...

    async def get_all_cursor[P: BaseEntity](
        self, filters: LayoutMessageCursorFiltersType, *, projection: type[P]
    ) -> CursorResult[P] | None: ...
