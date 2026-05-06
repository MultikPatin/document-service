from typing import TYPE_CHECKING, Protocol

from src.core.protocols.repository_methods import GetMixinProtocol

if TYPE_CHECKING:
    from src.domain.entities import BaseEntity
    from src.domain.models.pagination import (
        CursorResult,
        LimitOffsetResult,
        PagesResult,
    )
    from src.domain.protocols.pagination import (
        CursorParamsProtocol,
        LayoutFiltersProtocol,
        LimitOffsetParamsProtocol,
        PagesParamsProtocol,
    )


class LayoutRepositoryProtocol(GetMixinProtocol, Protocol):
    async def get_all_pages[R, S](
        self,
        filters: LayoutFiltersProtocol[PagesParamsProtocol],
        *,
        session: S,
        return_as: type[R],
    ) -> PagesResult[R] | None: ...
    async def get_all_limit_offset[R, S](
        self,
        filters: LayoutFiltersProtocol[LimitOffsetParamsProtocol],
        *,
        session: S,
        return_as: type[R],
    ) -> LimitOffsetResult[R] | None: ...
    async def get_all_cursor[R: BaseEntity, S](
        self,
        filters: LayoutFiltersProtocol[CursorParamsProtocol],
        *,
        session: S,
        return_as: type[R],
    ) -> CursorResult[R] | None: ...
