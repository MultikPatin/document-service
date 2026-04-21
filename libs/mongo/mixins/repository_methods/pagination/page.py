from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING, Any

from libs.core.dtos.pagination import PagesResultDTO
from libs.mongo.mixins.repository_methods import BaseRepository

from ._helpers import convert_items

if TYPE_CHECKING:
    from beanie.odm.enums import SortDirection
    from pydantic import BaseModel
    from pymongo.asynchronous.client_session import AsyncClientSession

    from libs.core.protocols.pagination import PagesParamsProtocol


class PaginationPagesMixin(BaseRepository):
    async def _get_all_pages[R, P: BaseModel](  # noqa: PLR0913
        self,
        conditions: Sequence[Mapping[Any, Any] | bool],
        params: PagesParamsProtocol,
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
    ) -> PagesResultDTO[R] | None:
        skip = (params.number - 1) * params.size
        limit = params.size

        documents = await self._document.find_many(
            *conditions,
            limit=limit,
            skip=skip,
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

        total_pages = total // params.size
        if params.size * total_pages < total:
            total_pages += 1
        next_page = (
            params.number + 1
            if total_pages > 1 and params.number < total_pages
            else None
        )
        previous_page = (
            params.number - 1 if total_pages > 1 and params.number > 1 else None
        )

        return PagesResultDTO(
            items=items,
            total=total_pages,
            current_page=params.number,
            previous_page=previous_page,
            next_page=next_page,
        )
