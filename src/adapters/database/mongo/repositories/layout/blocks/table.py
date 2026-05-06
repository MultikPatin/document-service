from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING, Any

from .base import LayoutBlockRepository

if TYPE_CHECKING:
    from pymongo.asynchronous.client_session import AsyncClientSession

    from src.domain.entities import BaseEntity
    from src.domain.models.pagination import (
        CursorResult,
        LimitOffsetResult,
        PagesResult,
    )
    from src.domain.protocols.pagination import (
        CursorParamsProtocol,
        LayoutBlockTableFiltersProtocol,
        LimitOffsetParamsProtocol,
        PagesParamsProtocol,
    )


class LayoutBlockTableRepository(LayoutBlockRepository):
    async def get_all_pages[R](
        self,
        filters: LayoutBlockTableFiltersProtocol[PagesParamsProtocol],
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
        filters: LayoutBlockTableFiltersProtocol[LimitOffsetParamsProtocol],
        *,
        session: AsyncClientSession,
        return_as: type[R],
    ) -> LimitOffsetResult[R] | None:
        return await self._get_all_limit_offset(
            conditions=self._pagination_conditions(filters),
            session=session,
            params=filters.pagination_params,
            return_as=return_as,
        )

    async def get_all_cursor[R: BaseEntity](
        self,
        filters: LayoutBlockTableFiltersProtocol[CursorParamsProtocol],
        *,
        session: AsyncClientSession,
        return_as: type[R],
    ) -> CursorResult[R] | None:
        return await self._get_all_cursor(
            conditions=self._pagination_conditions(filters),
            session=session,
            params=filters.pagination_params,
            return_as=return_as,
        )

    def _pagination_conditions(
        self, filters: LayoutBlockTableFiltersProtocol
    ) -> Sequence[Mapping[Any, Any] | bool]:
        conditions = []

        return conditions  # noqa: RET504
