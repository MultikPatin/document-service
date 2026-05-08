from typing import Protocol


class DeleteByIDMixinProtocol(Protocol):
    async def delete_by_id(self, id_: str) -> bool: ...
