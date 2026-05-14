from typing import TYPE_CHECKING

from src.domain.models.pagination import CursorResult
from src.infrastructure.mongo.contexts import PaginationQueryContex

from .base import BasePaginationMixin

if TYPE_CHECKING:
    from pydantic import BaseModel

    from src.domain.models.entities import BaseEntity
    from src.domain.protocols.pagination import CursorParamsProtocol
    from src.infrastructure.mongo.annotations import QueryConditionsType


class PaginationCursorMixin(BasePaginationMixin):
    async def _get_all_cursor[R: BaseEntity, P: BaseModel](
        self,
        conditions: QueryConditionsType,
        *,
        return_as: type[R],
        params: CursorParamsProtocol,
        projection: type[P] | None = None,
        ctx: PaginationQueryContex | None = None,
    ) -> CursorResult[R] | None:
        raise NotImplementedError

        if ctx is None:
            ctx = PaginationQueryContex()

        documents = await self._document.find_many(
            *conditions,
            # limit=limit,
            # skip=skip,
            session=self._session,
            projection_model=projection,
            sort=ctx.sort,
            ignore_cache=ctx.ignore_cache,
            fetch_links=ctx.fetch_links,
            with_children=ctx.with_children,
            nesting_depth=ctx.nesting_depth,
            nesting_depths_per_field=ctx.nesting_depths_per_field,
            lazy_parse=ctx.lazy_parse,
            **ctx.pymongo_kwargs,
        ).to_list()

        if not documents:
            return None

        count = await self._document.find(
            *conditions,
            session=self._session,
            ignore_cache=ctx.ignore_cache,
            fetch_links=ctx.fetch_links,
            **ctx.pymongo_kwargs,
        ).count()

        items = self._convert_items(documents, return_as, projection)
        return CursorResult.from_params(params, count, items)
