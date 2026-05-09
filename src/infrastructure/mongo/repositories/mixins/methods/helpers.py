from src.infrastructure.mongo.enums import KeyEnum
from src.infrastructure.mongo.repositories.mixins.base import (
    BaseRepository,
)


class ExistsMixin(BaseRepository):
    async def exists(self, id_: str) -> bool:
        return await self._document.find_one(
            {KeyEnum.id: self.converter.as_id(id_)}, session=self._session
        ).exists()


class CountMixin(BaseRepository):
    async def count(self, id_: str) -> int:
        return await self._document.find_one(
            {KeyEnum.id: self.converter.as_id(id_)}, session=self._session
        ).count()


# class IncRefCountMixin(BaseRepository):
#     async def inc_ref(self, id_: str) -> bool:
#         result = await self._document.find_one(
#             {KeyEnum.id: self.converter.as_id(id_)}, session=self._session
#         ).update({KeyEnum.inc: {"ref_count": 1}}, session=self._session)
#
#         return result.modified_count == 1
#
#
# class DecRefCountMixin(BaseRepository):
#     async def dec_ref(self, id_: str) -> bool:
#         result = await self._document.find_one(
#             {KeyEnum.id: self.converter.as_id(id_)}, session=self._session
#         ).update({KeyEnum.inc: {"ref_count": -1}}, session=self._session)
#
#         return result.modified_count == 1
