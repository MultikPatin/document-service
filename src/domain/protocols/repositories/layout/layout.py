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
    async def get_all_pages[R](
        self,
        filters: LayoutPageFiltersType,
        *,
        return_as: type[R],
    ) -> PagesResult[R] | None: ...
    async def get_all_limit_offset[R](
        self,
        filters: LayoutLimitOffsetFiltersType,
        *,
        return_as: type[R],
    ) -> LimitOffsetResult[R] | None: ...
    async def get_all_cursor[R: BaseEntity](
        self,
        filters: LayoutCursorFiltersType,
        *,
        return_as: type[R],
    ) -> CursorResult[R] | None: ...
