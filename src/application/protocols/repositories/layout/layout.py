from typing import TYPE_CHECKING, Protocol

from src.core.protocols.repository_methods import GetMixinProtocol

if TYPE_CHECKING:
    from src.application.protocols.pagination import (
        LayoutPaginationFiltersProtocol,
    )
    from src.core.dtos.pagination import (
        CursorResultDTO,
        LimitOffsetResultDTO,
        PagesResultDTO,
    )
    from src.core.protocols import (
        CursorParamsProtocol,
        LimitOffsetParamsProtocol,
        PagesParamsProtocol,
    )


class LayoutRepositoryProtocol(GetMixinProtocol, Protocol):
    async def get_all_pages[R, S](
        self,
        filters: LayoutPaginationFiltersProtocol[PagesParamsProtocol],
        *,
        session: S,
        return_as: type[R],
    ) -> PagesResultDTO[R] | None: ...
    async def get_all_limit_offset[R, S](
        self,
        filters: LayoutPaginationFiltersProtocol[LimitOffsetParamsProtocol],
        *,
        session: S,
        return_as: type[R],
    ) -> LimitOffsetResultDTO[R] | None: ...
    async def get_all_cursor[R, S](
        self,
        filters: LayoutPaginationFiltersProtocol[CursorParamsProtocol],
        *,
        session: S,
        return_as: type[R],
    ) -> CursorResultDTO[R] | None: ...
