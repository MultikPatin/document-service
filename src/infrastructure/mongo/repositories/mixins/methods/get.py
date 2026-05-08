import asyncio
from collections.abc import Sequence, Set

from src.domain.utils import batche_generator
from src.infrastructure.mongo.enums import KeyEnum
from src.infrastructure.mongo.repositories.mixins.repository import (
    BaseRepository,
)


class GetMixin(BaseRepository):
    async def get[R](self, id_: str, *, return_as: type[R]) -> R | None:
        document = await self._document.get(
            self.as_id(id_), session=self._session
        )
        if document is None:
            return None
        return self.as_dto(document, return_as, replace_links=True)


class GetByHashMixin(BaseRepository):
    async def get_by_hash[R](
        self, hash_string: str, *, return_as: type[R]
    ) -> R | None:
        document = await self._document.find_one(
            {"hash": hash_string}, session=self._session
        )
        if document is None:
            return None
        return self.as_dto(document, return_as, replace_links=True)


class GetByIDsMixin(BaseRepository):
    async def get_by_ids[R](
        self,
        ids: Set[str],
        *,
        return_as: type[R],
        batch_size: int | None = None,
        max_concurrent: int = 10,
    ) -> list[R] | None:
        semaphore = asyncio.Semaphore(max_concurrent)

        async def process(batche: Sequence[str]) -> list[R]:
            async with semaphore:
                documents = await self._document.find_many(
                    {KeyEnum.id: {KeyEnum.in_: self.as_ids(batche)}},
                    session=self._session,
                ).to_list()
                if not documents:
                    return []
                return self.as_dtos(documents, return_as, replace_links=True)

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
