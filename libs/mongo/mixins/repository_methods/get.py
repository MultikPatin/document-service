import asyncio
from collections.abc import Sequence, Set
from typing import TYPE_CHECKING

from libs.mongo.converters import (
    as_batches,
    to_dto,
    to_dtos,
    to_poid,
    to_poids,
)
from libs.mongo.enums import KeyEnum

from .base import BaseRepository

if TYPE_CHECKING:
    from pymongo.asynchronous.client_session import AsyncClientSession


class GetMixin(BaseRepository):
    async def get[ReturnSchema](
        self,
        document_id: str,
        *,
        session: AsyncClientSession | None = None,
        return_as: type[ReturnSchema],
    ) -> ReturnSchema | None:
        document = await self._document.find_one(
            {KeyEnum.id: to_poid(document_id)}, session=session
        )
        if document is None:
            return None
        return to_dto(document, return_as, replace_links=True)


class GetByHashMixin(BaseRepository):
    async def get_by_hash[ReturnSchema](
        self,
        hash_string: str,
        *,
        session: AsyncClientSession | None = None,
        return_as: type[ReturnSchema],
    ) -> ReturnSchema | None:
        document = await self._document.find_one(
            {"hash": hash_string}, session=session
        )
        if document is None:
            return None
        return to_dto(document, return_as, replace_links=True)


class GetByIDsMixin(BaseRepository):
    async def get_by_ids[ReturnSchema](
        self,
        document_ids: Set[str],
        *,
        session: AsyncClientSession | None = None,
        return_as: type[ReturnSchema],
        batch_size: int | None = None,
        max_concurrent: int = 10,
    ) -> list[ReturnSchema] | None:
        semaphore = asyncio.Semaphore(max_concurrent)

        async def process(batche: Sequence[str]) -> list[ReturnSchema]:
            async with semaphore:
                documents = await self._document.find_many(
                    {KeyEnum.id: {KeyEnum.in_: to_poids(batche)}},
                    session=session,
                ).to_list()
                if not documents:
                    return []
                return to_dtos(documents, return_as, replace_links=True)

        async with asyncio.TaskGroup() as tg:
            tasks = [
                tg.create_task(process(b))
                for b in as_batches(list(document_ids), batch_size)
            ]

        results = []
        for t in tasks:
            r = t.result()
            if r:
                results.extend(r)

        return results if results else None
