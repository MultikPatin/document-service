from typing import TYPE_CHECKING, Protocol

from src.core.protocols.repository_methods import (
    AddMixinProtocol,
    GetMixinProtocol,
)

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
    async def get_all_pages[R, S](
        self,
        filters: LayoutMessagePageFiltersType,
        *,
        session: S,
        return_as: type[R],
    ) -> PagesResult[R] | None: ...
    async def get_all_limit_offset[R, S](
        self,
        filters: LayoutMessageLimitOffsetFiltersType,
        *,
        session: S,
        return_as: type[R],
    ) -> LimitOffsetResult[R] | None: ...
    async def get_all_cursor[R: BaseEntity, S](
        self,
        filters: LayoutMessageCursorFiltersType,
        *,
        session: S,
        return_as: type[R],
    ) -> CursorResult[R] | None: ...


class LayoutBlockSingleRepositoryProtocol(BlockRepositoryProtocol, Protocol):
    async def get_all_pages[R, S](
        self,
        filters: LayoutSinglePageFiltersType,
        *,
        session: S,
        return_as: type[R],
    ) -> PagesResult[R] | None: ...
    async def get_all_limit_offset[R, S](
        self,
        filters: LayoutSingleLimitOffsetFiltersType,
        *,
        session: S,
        return_as: type[R],
    ) -> LimitOffsetResult[R] | None: ...
    async def get_all_cursor[R: BaseEntity, S](
        self,
        filters: LayoutSingleCursorFiltersType,
        *,
        session: S,
        return_as: type[R],
    ) -> CursorResult[R] | None: ...


class LayoutBlockTableRepositoryProtocol(BlockRepositoryProtocol, Protocol):
    async def get_all_pages[R, S](
        self,
        filters: LayoutTablePageFiltersType,
        *,
        session: S,
        return_as: type[R],
    ) -> PagesResult[R] | None: ...
    async def get_all_limit_offset[R, S](
        self,
        filters: LayoutTableLimitOffsetFiltersType,
        *,
        session: S,
        return_as: type[R],
    ) -> LimitOffsetResult[R] | None: ...
    async def get_all_cursor[R: BaseEntity, S](
        self,
        filters: LayoutTableCursorFiltersType,
        *,
        session: S,
        return_as: type[R],
    ) -> CursorResult[R] | None: ...
