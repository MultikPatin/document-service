from typing import Protocol


class DeleteByIDMixinProtocol(Protocol):
    async def delete_by_id[S](
        self, document_id: str, *, session: S
    ) -> bool: ...
