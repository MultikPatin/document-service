import asyncio
from collections.abc import Iterable, Sequence, Set
from typing import TYPE_CHECKING, Any

from beanie.odm.fields import WriteRules

from src.domain.utils import batche_generator
from src.infra.mongo.enums import KeyEnum

if TYPE_CHECKING:
    from beanie import Document, PydanticObjectId
    from beanie.odm.bulk import BulkWriter
    from pymongo.asynchronous.client_session import AsyncClientSession
    from pymongo.results import InsertManyResult


class Base[D: Document]:
    _document: type[D]
    _session: AsyncClientSession | None

    def __init__(self) -> None:
        self._session = None


# GET


class FindByID[D: Document](Base[D]):
    async def find_by_id(  # noqa: PLR0913
        self,
        document_id: PydanticObjectId,
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
            ignore_cache=ignore_cache,
            fetch_links=fetch_links,
            with_children=with_children,
            nesting_depth=nesting_depth,
            nesting_depths_per_field=nesting_depths_per_field,
            **pymongo_kwargs,
        )


class FindByHash[D: Document](Base[D]):
    async def find_by_hash(  # noqa: PLR0913
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


class FindByIDs[D: Document](Base[D]):
    async def find_by_ids(  # noqa: PLR0913
        self,
        ids: Set[PydanticObjectId],
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
            tasks = [
                tg.create_task(process(b))
                for b in batche_generator(list(ids), batch_size)
            ]

        results = []
        for t in tasks:
            r = t.result()
            if r:
                results.extend(r)

        return results if results else None


# INSERT


class InsertOne[D: Document](Base[D]):
    async def insert_one(
        self,
        document: D,
        *,
        bulk_writer: BulkWriter | None = None,
        link_rule: WriteRules = WriteRules.DO_NOTHING,
    ) -> D | None:
        await self._document.insert_one(
            document,
            session=self._session,
            bulk_writer=bulk_writer,
            link_rule=link_rule,
        )
        return document


class InsertMany[D: Document](Base[D]):
    async def _insert_many(self, documents: Iterable[D]) -> InsertManyResult:
        return await self._document.insert_many(
            documents, session=self._session
        )


# DELETE

# HELPERS


class ExistsByHash[D: Document](Base[D]):
    async def exists_by_hash(
        self,
        hash_string: str,
        *,
        ignore_cache: bool = False,
        **pymongo_kwargs: Any,  # noqa: ANN401
    ) -> bool:
        return await self._document.find_one(
            {"hash": hash_string},
            session=self._session,
            ignore_cache=ignore_cache,
            **pymongo_kwargs,
        ).exists()


class ExistsByID[D: Document](Base[D]):
    async def exists_by_id(
        self,
        document_id: PydanticObjectId,
        *,
        ignore_cache: bool = False,
        **pymongo_kwargs: Any,  # noqa: ANN401
    ) -> bool:
        return await self._document.find_one(
            {KeyEnum.id: document_id},
            session=self._session,
            ignore_cache=ignore_cache,
            **pymongo_kwargs,
        ).exists()
