from typing import TYPE_CHECKING

from src.domain.enums import LifeStatusEnum
from src.infra.mongo import interactors
from src.infra.mongo.documents import LayoutDocument
from src.infra.mongo.repositories import BaseRepository

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
    from src.domain.protocols.pagination import LayoutFiltersProtocol
    from src.infra.mongo.annotations import QueryConditionsType

type E = LayoutEntity
type D = LayoutDocument


class Layout(BaseRepository[D]):
    async def get(self, id_: str) -> E | None:
        interactor = interactors.FindByID[D](self._document, self._session)
        document = await interactor(id_)
        if document is None:
            return None
        return document.as_entity()

    async def get_all_pages[P: BaseModel](
        self, filters: LayoutPageFiltersType, *, projection: type[P]
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
        self, filters: LayoutLimitOffsetFiltersType, *, projection: type[P]
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
        self, filters: LayoutCursorFiltersType, *, projection: type[P]
    ) -> CursorResult[P] | None:
        interactor = interactors.PaginateAsCursor[D](
            self._document, self._session
        )
        return await interactor(
            self._pagination_conditions(filters),
            params=filters.pagination_params,
            projection=projection,
        )

    def _pagination_conditions(
        self, filters: LayoutFiltersProtocol
    ) -> QueryConditionsType:
        conditions = []

        if filters.status:
            conditions.append(self._document.status == filters.status)
        else:
            conditions.append(self._document.status == LifeStatusEnum.published)

        return conditions
