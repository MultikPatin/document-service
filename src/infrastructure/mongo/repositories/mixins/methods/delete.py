from src.infrastructure.mongo.enums import KeyEnum
from src.infrastructure.mongo.repositories.mixins.repository import (
    BaseRepository,
)


class DeleteByIDMixin(BaseRepository):
    async def delete_by_id(self, id_: str) -> bool:
        result = await self._document.find_one(
            {KeyEnum.id: self.as_id(id_)}
        ).delete(session=self._session)
        if result is None:
            return False
        return result.deleted_count == 1
