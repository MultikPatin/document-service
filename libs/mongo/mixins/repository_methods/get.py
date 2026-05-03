import asyncio
from collections.abc import Sequence, Set
from typing import TYPE_CHECKING

from libs.mongo.enums import KeyEnum
from src.core.batche import as_batches

from .base import BaseRepository

if TYPE_CHECKING:
    from pymongo.asynchronous.client_session import AsyncClientSession


class GetMixin(BaseRepository):
    async def get[R](
        self,
        document_id: str,
        *,
        session: AsyncClientSession,
        return_as: type[R],
    ) -> R | None:
        document = await self._document.get(
            self.as_id(document_id), session=session
        )
        if document is None:
            return None
        return self.as_dto(document, return_as, replace_links=True)


class GetByHashMixin(BaseRepository):
    async def get_by_hash[R](
        self,
        hash_string: str,
        *,
        session: AsyncClientSession,
        return_as: type[R],
    ) -> R | None:
        document = await self._document.find_one(
            {"hash": hash_string}, session=session
        )
        if document is None:
            return None
        return self.as_dto(document, return_as, replace_links=True)


class GetByIDsMixin(BaseRepository):
    async def get_by_ids[R](
        self,
        document_ids: Set[str],
        *,
        session: AsyncClientSession,
        return_as: type[R],
        batch_size: int | None = None,
        max_concurrent: int = 10,
    ) -> list[R] | None:
        semaphore = asyncio.Semaphore(max_concurrent)

        async def process(batche: Sequence[str]) -> list[R]:
            async with semaphore:
                documents = await self._document.find_many(
                    {KeyEnum.id: {KeyEnum.in_: self.as_ids(batche)}},
                    session=session,
                ).to_list()
                if not documents:
                    return []
                return self.as_dtos(documents, return_as, replace_links=True)

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
