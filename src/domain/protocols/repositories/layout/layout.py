from typing import TYPE_CHECKING, Protocol

from src.domain.protocols.methods import GetMixinProtocol

if TYPE_CHECKING:
    from src.domain.annotations import (
        LayoutCursorFiltersType,
        LayoutLimitOffsetFiltersType,
        LayoutPageFiltersType,
    )
    from src.domain.models.entities import BaseEntity
    from src.domain.models.pagination import (
        CursorResult,
        LimitOffsetResult,
        PagesResult,
    )


class LayoutRepositoryProtocol(GetMixinProtocol, Protocol):
    async def get_all_pages[R, S](
        self,
        filters: LayoutPageFiltersType,
        *,
        session: S,
        return_as: type[R],
    ) -> PagesResult[R] | None: ...
    async def get_all_limit_offset[R, S](
        self,
        filters: LayoutLimitOffsetFiltersType,
        *,
        session: S,
        return_as: type[R],
    ) -> LimitOffsetResult[R] | None: ...
    async def get_all_cursor[R: BaseEntity, S](
        self,
        filters: LayoutCursorFiltersType,
        *,
        session: S,
        return_as: type[R],
    ) -> CursorResult[R] | None: ...
