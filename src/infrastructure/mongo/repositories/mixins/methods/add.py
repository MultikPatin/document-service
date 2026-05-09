import asyncio
from collections.abc import Iterable
from typing import TYPE_CHECKING

from src.infrastructure.mongo.repositories.mixins.base import (
    BaseRepository,
)

if TYPE_CHECKING:
    from pydantic import BaseModel


class AddMixin(BaseRepository):
    async def add[R, C: BaseModel](
        self, condition: C, *, return_as: type[R]
    ) -> R:
        document = self._document(**condition.model_dump(exclude_none=True))
        await document.create(session=self._session)
        return self.converter.as_dto(document, return_as, replace_links=True)


class BulkAddWithReturnIdMixin(BaseRepository):
    async def bulk_add_with_return_id[C: BaseModel](
        self, conditions: Iterable[C]
    ) -> list[str]:
        documents = (
            self._document(**c.model_dump(exclude_none=True))
            for c in conditions
        )
        result = await self._document.insert_many(
            documents, session=self._session
        )
        return [str(_id) for _id in result.inserted_ids if _id is not None]


class BulkAddMixin(BaseRepository):
    async def bulk_add[R, C: BaseModel](
        self,
        conditions: Iterable[C],
        *,
        return_as: type[R],
        max_concurrent: int = 10,
    ) -> list[R]:
        if not conditions:
            return []

        semaphore = asyncio.Semaphore(max_concurrent)

        async def process(condition: C) -> R:
            async with semaphore:
                document = self._document(
                    **condition.model_dump(exclude_none=True)
                )
                await document.create(session=self._session)
                return self.converter.as_dto(
                    document, return_as, replace_links=True
                )

        async with asyncio.TaskGroup() as tg:
            tasks = [tg.create_task(process(b)) for b in conditions]

        return [t.result() for t in tasks]
