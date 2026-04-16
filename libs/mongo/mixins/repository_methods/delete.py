from typing import TYPE_CHECKING

from libs.mongo.converters import to_poid
from libs.mongo.enums import KeyEnum

from .base import BaseRepository

if TYPE_CHECKING:
    from pymongo.asynchronous.client_session import AsyncClientSession


class DeleteByIDMixin(BaseRepository):
    async def delete_by_id(
        self, _id: str, *, session: AsyncClientSession | None = None
    ) -> bool:
        result = await self._document.find_one(
            {KeyEnum.id: to_poid(_id)}
        ).delete(session=session)
        if result is None:
            return False
        return result.deleted_count == 1
