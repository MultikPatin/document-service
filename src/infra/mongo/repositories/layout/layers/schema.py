from collections.abc import Iterable
from typing import TYPE_CHECKING

from src.infra.mongo import interactors
from src.infra.mongo.repositories import BaseRepository

if TYPE_CHECKING:
    from src.domain.models.entities import LayoutLayerSchemaEntity
    from src.infra.mongo.documents import LayoutLayerSchemaDocument

type E = LayoutLayerSchemaEntity
type D = LayoutLayerSchemaDocument


class Shema(BaseRepository[D]):
    async def get(self, id_: str) -> E | None:
        interactor = interactors.FindByID[D](self._document, self._session)
        document = await interactor(id_)
        if document is None:
            return None
        return document.as_entity()

    async def get_by_ids(self, ids: Iterable[str]) -> list[E] | None:
        interactor = interactors.FindByIDs[D](self._document, self._session)
        documents = await interactor(ids)
        if documents is None:
            return None
        return [document.as_entity() for document in documents]

    async def get_by_hash(self, hash_string: str) -> E | None:
        interactor = interactors.FindByHash[D](self._document, self._session)
        document = await interactor(hash_string)
        if document is None:
            return None
        return document.as_entity()

    async def exists_by_hash(self, hash_string: str) -> bool:
        interactor = interactors.ExistsByHash[D](self._document, self._session)
        return await interactor(hash_string)

    # async def add[C](self, condition: C) -> E:
    #     pass
    #
    # async def delete[C](self, id_: str) -> bool:
    #     pass
