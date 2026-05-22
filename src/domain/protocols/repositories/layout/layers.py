from collections.abc import Iterable
from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from src.domain.models.entities import (
        BaseEntity,
        LayoutLayerDefaultEntity,
        LayoutLayerSchemaEntity,
        LayoutLayerValidationEntity,
    )


class LayerRepositoryProtocol[E: BaseEntity](Protocol):
    async def get(self, id_: str) -> E | None: ...
    async def get_by_ids(self, ids: Iterable[str]) -> list[E] | None: ...
    async def get_by_hash(self, hash_string: str) -> E | None: ...
    async def exists_by_hash(self, hash_string: str) -> bool: ...


class LayoutLayerDefaultRepositoryProtocol(
    LayerRepositoryProtocol[LayoutLayerDefaultEntity], Protocol
): ...


class LayoutLayerSchemaRepositoryProtocol(
    LayerRepositoryProtocol[LayoutLayerSchemaEntity], Protocol
): ...


class LayoutLayerValidationRepositoryProtocol(
    LayerRepositoryProtocol[LayoutLayerValidationEntity], Protocol
): ...
