import asyncio
from collections.abc import Iterable
from typing import TYPE_CHECKING

from libs.mongo.converters import to_dto

from .base import BaseRepository

if TYPE_CHECKING:
    from pydantic import BaseModel
    from pymongo.asynchronous.client_session import AsyncClientSession


class AddMixin(BaseRepository):
    async def add[ReturnSchema: BaseModel, CreateSchema: BaseModel](
        self,
        condition: CreateSchema,
        *,
        session: AsyncClientSession | None = None,
        return_as: type[ReturnSchema],
    ) -> ReturnSchema:
        document = self._document(**condition.model_dump(exclude_none=True))
        await document.create(session=session)
        return to_dto(document, return_as, replace_links=True)


class BulkAddWithReturnIdMixin(BaseRepository):
    async def bulk_add_with_return_id[CreateSchema: BaseModel](
        self,
        conditions: Iterable[CreateSchema],
        *,
        session: AsyncClientSession | None = None,
    ) -> list[str]:
        documents = (
            self._document(**c.model_dump(exclude_none=True))
            for c in conditions
        )
        result = await self._document.insert_many(documents, session=session)
        return [str(_id) for _id in result.inserted_ids if _id is not None]


class BulkAddMixin(BaseRepository):
    async def bulk_add[ReturnSchema: BaseModel, CreateSchema: BaseModel](
        self,
        conditions: Iterable[CreateSchema],
        *,
        session: AsyncClientSession | None = None,
        return_as: type[ReturnSchema],
        max_concurrent: int = 10,
    ) -> list[ReturnSchema]:
        semaphore = asyncio.Semaphore(max_concurrent)

        async def process(condition: CreateSchema) -> ReturnSchema:
            async with semaphore:
                document = self._document(
                    **condition.model_dump(exclude_none=True)
                )
                await document.create(session=session)
                return to_dto(document, return_as, replace_links=True)

        async with asyncio.TaskGroup() as tg:
            tasks = [tg.create_task(process(b)) for b in conditions]
            if not tasks:
                msg = (
                    "Must provide at least one condition to process in bulk_add"
                )
                # TODO: Реализовать специфическую ошибку
                raise ValueError(msg)

        return [t.result() for t in tasks]
