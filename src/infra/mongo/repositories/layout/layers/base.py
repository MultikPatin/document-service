from typing import TYPE_CHECKING

from src.infra.mongo.repositories.mixins import (
    AddMixin,
    # UpdateMixin,
    # DeleteWithRefCountMixin,
    GetByHashMixin,
    GetByIDsMixin,
    GetMixin,
)

if TYPE_CHECKING:
    from src.core.dtos import HashDTO


class LayoutLayerRepository(
    GetMixin,
    GetByIDsMixin,
    GetByHashMixin,
    AddMixin,
    # UpdateMixin,
    # DeleteWithRefCountMixin,
):
    async def add_by_hash[R, C: HashDTO](
        self, condition: C, *, return_as: type[R]
    ) -> R:
        result = await self.get_by_hash(
            hash_string=condition.get_hash(),
            return_as=return_as,
        )

        if result is None:
            document = self._document(**condition.model_dump(exclude_none=True))
            await document.create(session=self._session)
            result = self.converter.as_dto(
                document, return_as, replace_links=True
            )

        return result
