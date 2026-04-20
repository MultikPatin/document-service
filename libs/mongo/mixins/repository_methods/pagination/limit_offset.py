from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING, Any

from libs.core.dtos.pagination import LimitOffsetResultDTO
from libs.mongo.mixins.repository_methods import BaseRepository

from ._helpers import convert_items

if TYPE_CHECKING:
    from beanie.odm.enums import SortDirection
    from pydantic import BaseModel
    from pymongo.asynchronous.client_session import AsyncClientSession

    from libs.core.protocols.pagination import LimitOffsetParamsProtocol


class PaginationLimitOffsetMixin(BaseRepository):
    async def _get_all_limit_offset[R, P: BaseModel](  # noqa: PLR0913
        self,
        conditions: Sequence[Mapping[Any, Any] | bool],
        params: LimitOffsetParamsProtocol,
        session: AsyncClientSession,
        return_as: type[R],
        projection_model: type[P] | None = None,
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
            projection_model=projection_model,
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

        total = await self._document.find(
            *conditions,
            session=session,
            ignore_cache=ignore_cache,
            fetch_links=fetch_links,
            **pymongo_kwargs,
        ).count()

        is_projected = projection_model is not None
        items = convert_items(documents, return_as, is_projected)

        return LimitOffsetResultDTO(
            items=items,
            total=total,
            limit=params.limit,
            offset=params.offset,
        )
