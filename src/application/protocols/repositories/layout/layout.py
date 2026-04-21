from typing import TYPE_CHECKING, Protocol

from libs.core.protocols.repository_methods import GetMixinProtocol

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
        LayoutPaginationFiltersProtocol,
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
