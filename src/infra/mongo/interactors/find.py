import asyncio
from collections.abc import Iterable, Sequence
from typing import TYPE_CHECKING, Any

from src.domain.utils import batche_generator
from src.infra.mongo.enums import KeyEnum
from src.infra.mongo.utils import to_id

from .base import BaseInteractor

if TYPE_CHECKING:
    from beanie import Document, PydanticObjectId
    from pydantic import BaseModel

    from src.infra.mongo.annotations import QueryConditionsType, QuerySortType


class FindOne[D: Document, P: BaseModel](BaseInteractor[D]):
    async def __call__(  # noqa: PLR0913
        self,
        conditions: QueryConditionsType,
        *,
        projection: type[P] | None = None,
        limit: int,
        offset: int,
        ignore_cache: bool = False,
        fetch_links: bool = False,
        with_children: bool = False,
        lazy_parse: bool = False,
        nesting_depth: int | None = None,
        nesting_depths_per_field: dict[str, int] | None = None,
        **pymongo_kwargs: Any,  # noqa: ANN401
    ) -> D | None:
        return await self._document.find_one(
            *conditions,
            limit=limit,
            skip=offset,
            session=self._session,
            projection_model=projection,
            ignore_cache=ignore_cache,
            fetch_links=fetch_links,
            with_children=with_children,
            nesting_depth=nesting_depth,
            nesting_depths_per_field=nesting_depths_per_field,
            lazy_parse=lazy_parse,
            **pymongo_kwargs,
        )


class FindMany[D: Document, P: BaseModel](BaseInteractor[D]):
    async def __call__(  # noqa: PLR0913
        self,
        conditions: QueryConditionsType,
        *,
        projection: type[P] | None = None,
        limit: int,
        offset: int,
        sort: QuerySortType = None,
        ignore_cache: bool = False,
        fetch_links: bool = False,
        with_children: bool = False,
        lazy_parse: bool = False,
        nesting_depth: int | None = None,
        nesting_depths_per_field: dict[str, int] | None = None,
        **pymongo_kwargs: Any,  # noqa: ANN401
    ) -> list[D] | None:
        return await self._document.find_many(
            *conditions,
            limit=limit,
            skip=offset,
            session=self._session,
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


class FindByHash[D: Document](BaseInteractor[D]):
    async def __call__(  # noqa: PLR0913
        self,
        hash_string: str,
        *,
        ignore_cache: bool = False,
        fetch_links: bool = False,
        with_children: bool = False,
        nesting_depth: int | None = None,
        nesting_depths_per_field: dict[str, int] | None = None,
        **pymongo_kwargs: Any,  # noqa: ANN401
    ) -> D | None:
        return await self._document.find_one(
            {"hash": hash_string},
            session=self._session,
            ignore_cache=ignore_cache,
            fetch_links=fetch_links,
            with_children=with_children,
            nesting_depth=nesting_depth,
            nesting_depths_per_field=nesting_depths_per_field,
            **pymongo_kwargs,
        )


class FindByID[D: Document](BaseInteractor[D]):
    async def __call__(  # noqa: PLR0913
        self,
        document_id: Any,  # noqa: ANN401
        *,
        ignore_cache: bool = False,
        fetch_links: bool = False,
        with_children: bool = False,
        nesting_depth: int | None = None,
        nesting_depths_per_field: dict[str, int] | None = None,
        **pymongo_kwargs: Any,  # noqa: ANN401
    ) -> D | None:
        return await self._document.get(
            document_id,
            session=self._session,
            ignore_cache=ignore_cache,
            fetch_links=fetch_links,
            with_children=with_children,
            nesting_depth=nesting_depth,
            nesting_depths_per_field=nesting_depths_per_field,
            **pymongo_kwargs,
        )


class FindByIDs[D: Document](BaseInteractor[D]):
    async def __call__(  # noqa: PLR0913
        self,
        ids: Iterable[str],
        *,
        batch_size: int | None = None,
        max_concurrent: int = 10,
        ignore_cache: bool = False,
        fetch_links: bool = False,
        with_children: bool = False,
        nesting_depth: int | None = None,
        nesting_depths_per_field: dict[str, int] | None = None,
        **pymongo_kwargs: Any,  # noqa: ANN401
    ) -> list[D] | None:
        if not ids:
            return None

        unique = {to_id(i) for i in ids}
        batches = batche_generator(list(unique), batch_size)
        semaphore = asyncio.Semaphore(max_concurrent)

        async def process(batche: Sequence[PydanticObjectId]) -> list[D]:
            async with semaphore:
                return await self._document.find_many(
                    {KeyEnum.id: {KeyEnum.in_: batche}},
                    session=self._session,
                    ignore_cache=ignore_cache,
                    fetch_links=fetch_links,
                    with_children=with_children,
                    nesting_depth=nesting_depth,
                    nesting_depths_per_field=nesting_depths_per_field,
                    **pymongo_kwargs,
                ).to_list()

        async with asyncio.TaskGroup() as tg:
            tasks = [tg.create_task(process(b)) for b in batches]

        results = []
        for t in tasks:
            r = t.result()
            if r:
                results.extend(r)

        return results if results else None
