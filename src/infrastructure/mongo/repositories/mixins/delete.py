from typing import TYPE_CHECKING

from src.infrastructure.mongo.enums import KeyEnum

from .repository import BaseRepository

if TYPE_CHECKING:
    from pymongo.asynchronous.client_session import AsyncClientSession


class DeleteByIDMixin(BaseRepository):
    async def delete_by_id(
        self, document_id: str, *, session: AsyncClientSession | None = None
    ) -> bool:
        result = await self._document.find_one(
            {KeyEnum.id: self.as_id(document_id)}
        ).delete(session=session)
        if result is None:
            return False
        return result.deleted_count == 1
