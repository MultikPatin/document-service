from typing import TYPE_CHECKING

from libs.mongo.converters import to_dto
from libs.mongo.mixins.repository_methods import (
    AddMixin,
    # UpdateMixin,
    # DeleteWithRefCountMixin,
    DecRefCountMixin,
    GetByHashMixin,
    GetByIDsMixin,
    GetMixin,
    IncRefCountMixin,
)

if TYPE_CHECKING:
    from pymongo.asynchronous.client_session import AsyncClientSession

    from libs.core.dtos import HashDTO


class LayoutLayerRepository(
    GetMixin,
    GetByIDsMixin,
    GetByHashMixin,
    AddMixin,
    # UpdateMixin,
    # DeleteWithRefCountMixin,
    DecRefCountMixin,
    IncRefCountMixin,
):
    async def add_by_hash[R, C: HashDTO](
        self, condition: C, *, session: AsyncClientSession, return_as: type[R]
    ) -> R:
        result = await self.get_by_hash(
            hash_string=condition.get_hash(),
            session=session,
            return_as=return_as,
        )

        if result is None:
            document = self._document(**condition.model_dump(exclude_none=True))
            await document.create(session=session)
            result = to_dto(document, return_as, replace_links=True)

        return result
