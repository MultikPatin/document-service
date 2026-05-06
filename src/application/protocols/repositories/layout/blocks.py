from typing import TYPE_CHECKING, Protocol

from src.core.protocols.repository_methods import (
    AddMixinProtocol,
    GetMixinProtocol,
)

if TYPE_CHECKING:
    from src.application.protocols.pagination import (
        LayoutBlockMessagePaginationFiltersProtocol,
        LayoutBlockSinglePaginationFiltersProtocol,
        LayoutBlockTablePaginationFiltersProtocol,
    )
    from src.domain.entities import BaseEntity
    from src.domain.models.pagination import (
        CursorResult,
        LimitOffsetResult,
        PagesResult,
    )
    from src.domain.protocols.pagination import (
        CursorParamsProtocol,
        LimitOffsetParamsProtocol,
        PagesParamsProtocol,
    )


class BlockRepositoryProtocol(GetMixinProtocol, AddMixinProtocol, Protocol): ...


class LayoutBlockMessageRepositoryProtocol(BlockRepositoryProtocol, Protocol):
    async def get_all_pages[R, S](
        self,
        filters: LayoutBlockMessagePaginationFiltersProtocol[
            PagesParamsProtocol
        ],
        *,
        session: S,
        return_as: type[R],
    ) -> PagesResult[R] | None: ...
    async def get_all_limit_offset[R, S](
        self,
        filters: LayoutBlockMessagePaginationFiltersProtocol[
            LimitOffsetParamsProtocol
        ],
        *,
        session: S,
        return_as: type[R],
    ) -> LimitOffsetResult[R] | None: ...
    async def get_all_cursor[R: BaseEntity, S](
        self,
        filters: LayoutBlockMessagePaginationFiltersProtocol[
            CursorParamsProtocol
        ],
        *,
        session: S,
        return_as: type[R],
    ) -> CursorResult[R] | None: ...


class LayoutBlockSingleRepositoryProtocol(BlockRepositoryProtocol, Protocol):
    async def get_all_pages[R, S](
        self,
        filters: LayoutBlockSinglePaginationFiltersProtocol[
            PagesParamsProtocol
        ],
        *,
        session: S,
        return_as: type[R],
    ) -> PagesResult[R] | None: ...
    async def get_all_limit_offset[R, S](
        self,
        filters: LayoutBlockSinglePaginationFiltersProtocol[
            LimitOffsetParamsProtocol
        ],
        *,
        session: S,
        return_as: type[R],
    ) -> LimitOffsetResult[R] | None: ...
    async def get_all_cursor[R: BaseEntity, S](
        self,
        filters: LayoutBlockSinglePaginationFiltersProtocol[
            CursorParamsProtocol
        ],
        *,
        session: S,
        return_as: type[R],
    ) -> CursorResult[R] | None: ...


class LayoutBlockTableRepositoryProtocol(BlockRepositoryProtocol, Protocol):
    async def get_all_pages[R, S](
        self,
        filters: LayoutBlockTablePaginationFiltersProtocol[PagesParamsProtocol],
        *,
        session: S,
        return_as: type[R],
    ) -> PagesResult[R] | None: ...
    async def get_all_limit_offset[R, S](
        self,
        filters: LayoutBlockTablePaginationFiltersProtocol[
            LimitOffsetParamsProtocol
        ],
        *,
        session: S,
        return_as: type[R],
    ) -> LimitOffsetResult[R] | None: ...
    async def get_all_cursor[R: BaseEntity, S](
        self,
        filters: LayoutBlockTablePaginationFiltersProtocol[
            CursorParamsProtocol
        ],
        *,
        session: S,
        return_as: type[R],
    ) -> CursorResult[R] | None: ...
