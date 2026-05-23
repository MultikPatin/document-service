from typing import TYPE_CHECKING

from src.infra.mongo import interactors
from src.infra.mongo.repositories import BaseRepository

if TYPE_CHECKING:
    from pydantic import BaseModel

    from src.domain.annotations import (
        LayoutMessageCursorFiltersType,
        LayoutMessageLimitOffsetFiltersType,
        LayoutMessagePageFiltersType,
    )
    from src.domain.models.entities import BaseEntity, LayoutBlockMessageEntity
    from src.domain.models.pagination import (
        CursorResult,
        LimitOffsetResult,
        PagesResult,
    )
    from src.domain.protocols.pagination import (
        LayoutBlockMessageFiltersProtocol,
    )
    from src.infra.mongo.annotations import QueryConditionsType
    from src.infra.mongo.documents import LayoutBlockMessageDocument

type E = LayoutBlockMessageEntity
type D = LayoutBlockMessageDocument


class Message(BaseRepository[D]):
    async def get(self, id_: str) -> E | None:
        interactor = interactors.FindByID[D](self._document, self._session)
        document = await interactor(id_)
        if document is None:
            return None
        return document.as_entity()

    async def get_all_pages[P: BaseModel](
        self, filters: LayoutMessagePageFiltersType, *, projection: type[P]
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
        filters: LayoutMessageLimitOffsetFiltersType,
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
        self, filters: LayoutMessageCursorFiltersType, *, projection: type[P]
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
        self, filters: LayoutBlockMessageFiltersProtocol
    ) -> QueryConditionsType:
        conditions = []

        return conditions  # noqa: RET504
