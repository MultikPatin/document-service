from typing import TYPE_CHECKING, Protocol

from src.domain.protocols.methods import (
    AddMixinProtocol,
    # UpdateMixinProtocol,
    # DeleteWithRefCountMixinProtocol,
    GetByHashMixinProtocol,
    GetByIDsMixinProtocol,
    GetMixinProtocol,
)

if TYPE_CHECKING:
    from src.domain.models.dtos import HashDTO


class LayerRepositoryProtocol(
    GetMixinProtocol,
    GetByIDsMixinProtocol,
    GetByHashMixinProtocol,
    AddMixinProtocol,
    # UpdateMixinProtocol,
    # DeleteWithRefCountMixinProtocol,
    Protocol,
):
    async def add_by_hash[R, C: HashDTO](
        self, condition: C, *, return_as: type[R]
    ) -> R: ...


class LayoutLayerDefaultRepositoryProtocol(
    LayerRepositoryProtocol, Protocol
): ...


class LayoutLayerSchemaRepositoryProtocol(
    LayerRepositoryProtocol, Protocol
): ...


class LayoutLayerValidationRepositoryProtocol(
    LayerRepositoryProtocol, Protocol
): ...
