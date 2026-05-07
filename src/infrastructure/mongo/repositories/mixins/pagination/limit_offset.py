from collections.abc import Sequence
from typing import TYPE_CHECKING, Any

from src.domain.models.pagination import LimitOffsetResult

from .base import BasePaginationMixin

if TYPE_CHECKING:
    from beanie.odm.enums import SortDirection
    from pydantic import BaseModel
    from pymongo.asynchronous.client_session import AsyncClientSession

    from src.domain.protocols.pagination import LimitOffsetParamsProtocol
    from src.infrastructure.mongo.annotations import QueryConditionsType


class PaginationLimitOffsetMixin(BasePaginationMixin):
    async def _get_all_limit_offset[R, P: BaseModel](  # noqa: PLR0913
        self,
        conditions: QueryConditionsType,
        params: LimitOffsetParamsProtocol,
        session: AsyncClientSession,
        return_as: type[R],
        projection: type[P] | None = None,
        sort: str | Sequence[tuple[str, SortDirection]] | None = None,
        ignore_cache: bool = False,
        fetch_links: bool = False,
        with_children: bool = False,
        lazy_parse: bool = False,
        nesting_depth: int | None = None,
        nesting_depths_per_field: dict[str, int] | None = None,
        **pymongo_kwargs: Any,  # noqa: ANN401
    ) -> LimitOffsetResult[R] | None:

        documents = await self._document.find_many(
            *conditions,
            limit=params.limit,
            skip=params.offset,
            session=session,
            projection_model=projection,
            sort=sort,
            ignore_cache=ignore_cache,
            fetch_links=fetch_links,
            with_children=with_children,
            nesting_depth=nesting_depth,
            nesting_depths_per_field=nesting_depths_per_field,
            lazy_parse=lazy_parse,
            **pymongo_kwargs,
        ).to_list()

        if not documents:
            return None

        count = await self._document.find(
            *conditions,
            session=session,
            ignore_cache=ignore_cache,
            fetch_links=fetch_links,
            **pymongo_kwargs,
        ).count()

        return LimitOffsetResult.from_params(
            params, count, self._convert_items(documents, return_as, projection)
        )
