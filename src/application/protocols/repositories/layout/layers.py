from typing import TYPE_CHECKING, Protocol

from libs.core.protocols.repository_methods import (
    AddMixinProtocol,
    # UpdateMixinProtocol,
    # DeleteWithRefCountMixinProtocol,
    DecRefCountMixinProtocol,
    GetByHashMixinProtocol,
    GetByIDsMixinProtocol,
    GetMixinProtocol,
    IncRefCountMixinProtocol,
)

if TYPE_CHECKING:
    from libs.core.dtos import HashDTO


class LayerRepositoryProtocol(
    GetMixinProtocol,
    GetByIDsMixinProtocol,
    GetByHashMixinProtocol,
    AddMixinProtocol,
    # UpdateMixinProtocol,
    # DeleteWithRefCountMixinProtocol,
    DecRefCountMixinProtocol,
    IncRefCountMixinProtocol,
    Protocol,
):
    async def add_by_hash[R, S, C: HashDTO](
        self, condition: C, *, session: S, return_as: type[R]
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
