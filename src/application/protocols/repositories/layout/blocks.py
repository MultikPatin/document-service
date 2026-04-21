from typing import TYPE_CHECKING, Protocol

from libs.core.protocols.repository_methods import (
    AddMixinProtocol,
    GetMixinProtocol,
)

if TYPE_CHECKING:
    from libs.core.dtos.pagination import (
        CursorResultDTO,
        LimitOffsetResultDTO,
        PagesResultDTO,
    )
    from libs.core.protocols.pagination import (
        CursorParamsProtocol,
        LimitOffsetParamsProtocol,
        PagesParamsProtocol,
    )
    from src.application.protocols.pagination import (
        LayoutBlockMessagePaginationFiltersProtocol,
        LayoutBlockSinglePaginationFiltersProtocol,
        LayoutBlockTablePaginationFiltersProtocol,
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
    ) -> PagesResultDTO[R] | None: ...
    async def get_all_limit_offset[R, S](
        self,
        filters: LayoutBlockMessagePaginationFiltersProtocol[
            LimitOffsetParamsProtocol
        ],
        *,
        session: S,
        return_as: type[R],
    ) -> LimitOffsetResultDTO[R] | None: ...
    async def get_all_cursor[R, S](
        self,
        filters: LayoutBlockMessagePaginationFiltersProtocol[
            CursorParamsProtocol
        ],
        *,
        session: S,
        return_as: type[R],
    ) -> CursorResultDTO[R] | None: ...


class LayoutBlockSingleRepositoryProtocol(BlockRepositoryProtocol, Protocol):
    async def get_all_pages[R, S](
        self,
        filters: LayoutBlockSinglePaginationFiltersProtocol[
            PagesParamsProtocol
        ],
        *,
        session: S,
        return_as: type[R],
    ) -> PagesResultDTO[R] | None: ...
    async def get_all_limit_offset[R, S](
        self,
        filters: LayoutBlockSinglePaginationFiltersProtocol[
            LimitOffsetParamsProtocol
        ],
        *,
        session: S,
        return_as: type[R],
    ) -> LimitOffsetResultDTO[R] | None: ...
    async def get_all_cursor[R, S](
        self,
        filters: LayoutBlockSinglePaginationFiltersProtocol[
            CursorParamsProtocol
        ],
        *,
        session: S,
        return_as: type[R],
    ) -> CursorResultDTO[R] | None: ...


class LayoutBlockTableRepositoryProtocol(BlockRepositoryProtocol, Protocol):
    async def get_all_pages[R, S](
        self,
        filters: LayoutBlockTablePaginationFiltersProtocol[PagesParamsProtocol],
        *,
        session: S,
        return_as: type[R],
    ) -> PagesResultDTO[R] | None: ...
    async def get_all_limit_offset[R, S](
        self,
        filters: LayoutBlockTablePaginationFiltersProtocol[
            LimitOffsetParamsProtocol
        ],
        *,
        session: S,
        return_as: type[R],
    ) -> LimitOffsetResultDTO[R] | None: ...
    async def get_all_cursor[R, S](
        self,
        filters: LayoutBlockTablePaginationFiltersProtocol[
            CursorParamsProtocol
        ],
        *,
        session: S,
        return_as: type[R],
    ) -> CursorResultDTO[R] | None: ...
