from collections.abc import Iterable

from src.domain.models.entities import LayoutLayerSchemaEntity
from src.domain.protocols.repositories import (
    LayoutLayerSchemaRepositoryProtocol,
)

type Entity = LayoutLayerSchemaEntity


class LayoutLayerSchemaService:
    def __init__(self, repo: LayoutLayerSchemaRepositoryProtocol) -> None:
        self._repo = repo

    async def get(self, id_: str) -> Entity | None:
        return await self._repo.get(id_)

    async def get_by_ids(self, ids: Iterable[str]) -> list[Entity] | None:
        return await self._repo.get_by_ids(ids)

    async def get_by_hash(self, hash_: str) -> Entity | None:
        return await self._repo.get_by_hash(hash_)

    async def exists_by_hash(self, hash_: str) -> bool:
        return await self._repo.exists_by_hash(hash_)
