from typing import Protocol

from src.domain.protocols.methods import AddMixinProtocol, GetMixinProtocol


class ReportRepositoryProtocol(GetMixinProtocol, AddMixinProtocol, Protocol):
    async def get_full_links[R](
        self, id_: str, *, return_as: type[R]
    ) -> R | None: ...
    async def get_layout_id(self, id_: str) -> str | None: ...
