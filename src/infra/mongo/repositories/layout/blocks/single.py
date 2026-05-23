from typing import TYPE_CHECKING

from src.infra.mongo import interactors
from src.infra.mongo.repositories import BaseRepository

if TYPE_CHECKING:
    from pydantic import BaseModel

    from src.domain.annotations import (
        LayoutSingleCursorFiltersType,
        LayoutSingleLimitOffsetFiltersType,
        LayoutSinglePageFiltersType,
    )
    from src.domain.models.entities import BaseEntity, LayoutBlockSingleEntity
    from src.domain.models.pagination import (
        CursorResult,
        LimitOffsetResult,
        PagesResult,
    )
    from src.domain.protocols.pagination import (
        LayoutBlockSingleFiltersProtocol,
    )
    from src.infra.mongo.annotations import QueryConditionsType
    from src.infra.mongo.documents import LayoutBlockSingleDocument


type E = LayoutBlockSingleEntity
type D = LayoutBlockSingleDocument


class Single(BaseRepository[D]):
    async def get(self, id_: str) -> E | None:
        interactor = interactors.FindByID[D](self._document, self._session)
        document = await interactor(id_)
        if document is None:
            return None
        return document.as_entity()

    async def get_all_pages[P: BaseModel](
        self, filters: LayoutSinglePageFiltersType, *, projection: type[P]
    ) -> PagesResult[P] | None:
        interactor = interactors.PaginateAsPages[D](
            self._document, self._session
        )
        return await interactor(
            self._pagination_conditions(filters),
            params=filters.pagination_params,
            projection=projection,
        )

    async def get_all_limit_offset[P: BaseModel](
        self,
        filters: LayoutSingleLimitOffsetFiltersType,
        *,
        projection: type[P],
    ) -> LimitOffsetResult[P] | None:
        interactor = interactors.PaginateAsLimitOffset[D](
            self._document, self._session
        )
        return await interactor(
            self._pagination_conditions(filters),
            params=filters.pagination_params,
            projection=projection,
        )

    async def get_all_cursor[P: BaseEntity](
        self, filters: LayoutSingleCursorFiltersType, *, projection: type[P]
    ) -> CursorResult[P] | None:
        interactor = interactors.PaginateAsCursor[D](
            self._document, self._session
        )
        return await interactor(
            self._pagination_conditions(filters),
            params=filters.pagination_params,
            projection=projection,
        )

    # async def add[C](self, condition: C) -> E:
    #     pass

    def _pagination_conditions(
        self, filters: LayoutBlockSingleFiltersProtocol
    ) -> QueryConditionsType:
        conditions = []

        return conditions  # noqa: RET504
