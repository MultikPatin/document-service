from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from pydantic import BaseModel

    from src.domain.annotations import (
        LayoutCursorFiltersType,
        LayoutLimitOffsetFiltersType,
        LayoutPageFiltersType,
    )
    from src.domain.models.entities import BaseEntity, LayoutEntity
    from src.domain.models.pagination import (
        CursorResult,
        LimitOffsetResult,
        PagesResult,
    )


class LayoutRepositoryProtocol[E: LayoutEntity](Protocol):
    async def get(self, id_: str) -> E | None: ...
    async def get_all_pages[P: BaseModel](
        self, filters: LayoutPageFiltersType, *, projection: type[P]
    ) -> PagesResult[P] | None: ...

    async def get_all_limit_offset[P: BaseModel](
        self, filters: LayoutLimitOffsetFiltersType, *, projection: type[P]
    ) -> LimitOffsetResult[P] | None: ...

    async def get_all_cursor[P: BaseEntity](
        self, filters: LayoutCursorFiltersType, *, projection: type[P]
    ) -> CursorResult[P] | None: ...
