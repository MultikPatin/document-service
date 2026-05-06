from typing import TYPE_CHECKING, Protocol

from src.core.protocols.repository_methods import (
    AddMixinProtocol,
    GetMixinProtocol,
)

if TYPE_CHECKING:
    from src.domain.entities import BaseEntity
    from src.domain.models.pagination import (
        CursorResult,
        LimitOffsetResult,
        PagesResult,
    )
    from src.domain.protocols.pagination import (
        CursorParamsProtocol,
        LayoutBlockMessageFiltersProtocol,
        LayoutBlockSingleFiltersProtocol,
        LayoutBlockTableFiltersProtocol,
        LimitOffsetParamsProtocol,
        PagesParamsProtocol,
    )


class BlockRepositoryProtocol(GetMixinProtocol, AddMixinProtocol, Protocol): ...


class LayoutBlockMessageRepositoryProtocol(BlockRepositoryProtocol, Protocol):
    async def get_all_pages[R, S](
        self,
        filters: LayoutBlockMessageFiltersProtocol[PagesParamsProtocol],
        *,
        session: S,
        return_as: type[R],
    ) -> PagesResult[R] | None: ...
    async def get_all_limit_offset[R, S](
        self,
        filters: LayoutBlockMessageFiltersProtocol[LimitOffsetParamsProtocol],
        *,
        session: S,
        return_as: type[R],
    ) -> LimitOffsetResult[R] | None: ...
    async def get_all_cursor[R: BaseEntity, S](
        self,
        filters: LayoutBlockMessageFiltersProtocol[CursorParamsProtocol],
        *,
        session: S,
        return_as: type[R],
    ) -> CursorResult[R] | None: ...


class LayoutBlockSingleRepositoryProtocol(BlockRepositoryProtocol, Protocol):
    async def get_all_pages[R, S](
        self,
        filters: LayoutBlockSingleFiltersProtocol[PagesParamsProtocol],
        *,
        session: S,
        return_as: type[R],
    ) -> PagesResult[R] | None: ...
    async def get_all_limit_offset[R, S](
        self,
        filters: LayoutBlockSingleFiltersProtocol[LimitOffsetParamsProtocol],
        *,
        session: S,
        return_as: type[R],
    ) -> LimitOffsetResult[R] | None: ...
    async def get_all_cursor[R: BaseEntity, S](
        self,
        filters: LayoutBlockSingleFiltersProtocol[CursorParamsProtocol],
        *,
        session: S,
        return_as: type[R],
    ) -> CursorResult[R] | None: ...


class LayoutBlockTableRepositoryProtocol(BlockRepositoryProtocol, Protocol):
    async def get_all_pages[R, S](
        self,
        filters: LayoutBlockTableFiltersProtocol[PagesParamsProtocol],
        *,
        session: S,
        return_as: type[R],
    ) -> PagesResult[R] | None: ...
    async def get_all_limit_offset[R, S](
        self,
        filters: LayoutBlockTableFiltersProtocol[LimitOffsetParamsProtocol],
        *,
        session: S,
        return_as: type[R],
    ) -> LimitOffsetResult[R] | None: ...
    async def get_all_cursor[R: BaseEntity, S](
        self,
        filters: LayoutBlockTableFiltersProtocol[CursorParamsProtocol],
        *,
        session: S,
        return_as: type[R],
    ) -> CursorResult[R] | None: ...
