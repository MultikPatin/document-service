from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING, Any

from src.core.dtos.pagination import LimitOffsetResultDTO

from .base import BasePaginationMixin

if TYPE_CHECKING:
    from beanie.odm.enums import SortDirection
    from pydantic import BaseModel
    from pymongo.asynchronous.client_session import AsyncClientSession

    from src.core.protocols import LimitOffsetParamsProtocol


class PaginationLimitOffsetMixin(BasePaginationMixin):
    async def _get_all_limit_offset[R, P: BaseModel](  # noqa: PLR0913
        self,
        conditions: Sequence[Mapping[Any, Any] | bool],
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
    ) -> LimitOffsetResultDTO[R] | None:

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

        return LimitOffsetResultDTO.from_params(
            params, count, self._convert_items(documents, return_as, projection)
        )
