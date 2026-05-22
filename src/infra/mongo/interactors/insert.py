from collections.abc import Iterable
from typing import TYPE_CHECKING

from beanie.odm.fields import WriteRules

if TYPE_CHECKING:
    from beanie import Document
    from beanie.odm.bulk import BulkWriter
    from pymongo.results import InsertManyResult

from .base import BaseInteractor


class InsertOne[D: Document](BaseInteractor[D]):
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


class InsertMany[D: Document](BaseInteractor[D]):
    async def _insert_many(self, documents: Iterable[D]) -> InsertManyResult:
        return await self._document.insert_many(
            documents, session=self._session
        )
