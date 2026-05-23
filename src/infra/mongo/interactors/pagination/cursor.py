from typing import TYPE_CHECKING

from src.domain.models.pagination import CursorResult
from src.infra.mongo.contexts import PaginationQueryContex
from src.infra.mongo.interactors.base import BaseInteractor
from src.infra.mongo.interactors.find import FindMany
from src.infra.mongo.interactors.helpers import CountByConditions

if TYPE_CHECKING:
    from beanie import Document

    from src.domain.models.entities import BaseEntity
    from src.domain.protocols.pagination import CursorParamsProtocol
    from src.infra.mongo.annotations import QueryConditionsType


class PaginateAsCursor[D: Document](BaseInteractor[D]):
    async def __call__[P: BaseEntity](
        self,
        conditions: QueryConditionsType,
        *,
        params: CursorParamsProtocol,
        projection: type[P],
        ctx: PaginationQueryContex | None = None,
    ) -> CursorResult[P] | None:
        raise NotImplementedError

        if ctx is None:
            ctx = PaginationQueryContex()

        interactor = CountByConditions[D](self._document, self._session)
        count = await interactor(
            conditions,
            ignore_cache=ctx.ignore_cache,
            fetch_links=ctx.fetch_links,
            **ctx.pymongo_kwargs,
        )

        interactor = FindMany[D, P](self._document, self._session)
        items = await interactor(
            conditions,
            limit=params.limit,
            skip=params.offset,
            projection_model=projection,
            sort=ctx.sort,
            ignore_cache=ctx.ignore_cache,
            fetch_links=ctx.fetch_links,
            with_children=ctx.with_children,
            nesting_depth=ctx.nesting_depth,
            nesting_depths_per_field=ctx.nesting_depths_per_field,
            lazy_parse=ctx.lazy_parse,
            **ctx.pymongo_kwargs,
        )

        if not items:
            return None

        return CursorResult.from_params(params, count, items)
