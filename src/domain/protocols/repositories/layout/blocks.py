from typing import TYPE_CHECKING, Protocol

from src.domain.protocols.methods import AddMixinProtocol, GetMixinProtocol

if TYPE_CHECKING:
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


class BlockRepositoryProtocol(GetMixinProtocol, AddMixinProtocol, Protocol): ...


class LayoutBlockMessageRepositoryProtocol(BlockRepositoryProtocol, Protocol):
    async def get_all_pages[R](
        self,
        filters: LayoutMessagePageFiltersType,
        *,
        return_as: type[R],
    ) -> PagesResult[R] | None: ...
    async def get_all_limit_offset[R](
        self,
        filters: LayoutMessageLimitOffsetFiltersType,
        *,
        return_as: type[R],
    ) -> LimitOffsetResult[R] | None: ...
    async def get_all_cursor[R: BaseEntity](
        self,
        filters: LayoutMessageCursorFiltersType,
        *,
        return_as: type[R],
    ) -> CursorResult[R] | None: ...


class LayoutBlockSingleRepositoryProtocol(BlockRepositoryProtocol, Protocol):
    async def get_all_pages[R](
        self,
        filters: LayoutSinglePageFiltersType,
        *,
        return_as: type[R],
    ) -> PagesResult[R] | None: ...
    async def get_all_limit_offset[R](
        self,
        filters: LayoutSingleLimitOffsetFiltersType,
        *,
        return_as: type[R],
    ) -> LimitOffsetResult[R] | None: ...
    async def get_all_cursor[R: BaseEntity](
        self,
        filters: LayoutSingleCursorFiltersType,
        *,
        return_as: type[R],
    ) -> CursorResult[R] | None: ...


class LayoutBlockTableRepositoryProtocol(BlockRepositoryProtocol, Protocol):
    async def get_all_pages[R](
        self,
        filters: LayoutTablePageFiltersType,
        *,
        return_as: type[R],
    ) -> PagesResult[R] | None: ...
    async def get_all_limit_offset[R](
        self,
        filters: LayoutTableLimitOffsetFiltersType,
        *,
        return_as: type[R],
    ) -> LimitOffsetResult[R] | None: ...
    async def get_all_cursor[R: BaseEntity](
        self,
        filters: LayoutTableCursorFiltersType,
        *,
        return_as: type[R],
    ) -> CursorResult[R] | None: ...
