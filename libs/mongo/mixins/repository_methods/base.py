from typing import TYPE_CHECKING

from libs.mongo.converters import to_poid
from libs.mongo.enums import KeyEnum

if TYPE_CHECKING:
    from beanie import Document
    from pymongo.asynchronous.client_session import AsyncClientSession


class BaseRepository:
    def __init__[DocType: Document](self, document: type[DocType]) -> None:
        self._document = document


class ExistsMixin(BaseRepository):
    async def exists(
        self, document_id: str, *, session: AsyncClientSession
    ) -> bool:
        return await self._document.find_one(
            {KeyEnum.id: to_poid(document_id)}, session=session
        ).exists()


class CountMixin(BaseRepository):
    async def count(
        self, document_id: str, *, session: AsyncClientSession
    ) -> int:
        return await self._document.find_one(
            {KeyEnum.id: to_poid(document_id)}, session=session
        ).count()


class IncRefCountMixin(BaseRepository):
    async def inc_ref(
        self, document_id: str, *, session: AsyncClientSession
    ) -> bool:
        result = await self._document.find_one(
            {KeyEnum.id: to_poid(document_id)}, session=session
        ).update({KeyEnum.inc: {"ref_count": 1}}, session=session)

        return result.modified_count == 1


class DecRefCountMixin(BaseRepository):
    async def dec_ref(
        self, document_id: str, *, session: AsyncClientSession
    ) -> bool:
        result = await self._document.find_one(
            {KeyEnum.id: to_poid(document_id)}, session=session
        ).update({KeyEnum.inc: {"ref_count": -1}}, session=session)

        return result.modified_count == 1
