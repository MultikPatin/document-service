from typing import TYPE_CHECKING

from .base import LayoutBlockRepository

if TYPE_CHECKING:
    from pymongo.asynchronous.client_session import AsyncClientSession

    from src.domain.annotations import (
        LayoutMessageCursorFiltersType,
        LayoutMessageLimitOffsetFiltersType,
        LayoutMessagePageFiltersType,
    )
    from src.domain.models.entities import BaseEntity
    from src.domain.models.pagination import (
        CursorResult,
        LimitOffsetResult,
        PagesResult,
    )
    from src.domain.protocols.pagination import (
        LayoutBlockMessageFiltersProtocol,
    )
    from src.infrastructure.mongo.annotations import QueryConditionsType


class LayoutBlockMessageRepository(LayoutBlockRepository):
    async def get_all_pages[R](
        self,
        filters: LayoutMessagePageFiltersType,
        *,
        session: AsyncClientSession,
        return_as: type[R],
    ) -> PagesResult[R] | None:
        return await self._get_all_pages(
            conditions=self._pagination_conditions(filters),
            params=filters.pagination_params,
            session=session,
            return_as=return_as,
        )

    async def get_all_limit_offset[R](
        self,
        filters: LayoutMessageLimitOffsetFiltersType,
        *,
        session: AsyncClientSession,
        return_as: type[R],
    ) -> LimitOffsetResult[R] | None:
        return await self._get_all_limit_offset(
            conditions=self._pagination_conditions(filters),
            params=filters.pagination_params,
            session=session,
            return_as=return_as,
        )

    async def get_all_cursor[R: BaseEntity](
        self,
        filters: LayoutMessageCursorFiltersType,
        *,
        session: AsyncClientSession,
        return_as: type[R],
    ) -> CursorResult[R] | None:
        return await self._get_all_cursor(
            conditions=self._pagination_conditions(filters),
            params=filters.pagination_params,
            session=session,
            return_as=return_as,
        )

    def _pagination_conditions(
        self, filters: LayoutBlockMessageFiltersProtocol
    ) -> QueryConditionsType:
        conditions = []

        return conditions  # noqa: RET504
