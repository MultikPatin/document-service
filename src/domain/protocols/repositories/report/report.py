from typing import Protocol

from src.domain.protocols.methods import AddMixinProtocol, GetMixinProtocol


class ReportRepositoryProtocol(GetMixinProtocol, AddMixinProtocol, Protocol):
    async def get_full_links[R, S](
        self, document_id: str, *, session: S, return_as: type[R]
    ) -> R | None: ...
    async def get_layout_id[S](
        self, document_id: str, *, session: S
    ) -> str | None: ...
