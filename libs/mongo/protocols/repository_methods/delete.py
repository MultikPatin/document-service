from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from pymongo.asynchronous.client_session import AsyncClientSession


class DeleteByIDMixinProtocol(Protocol):
    async def delete_by_id(
        self, document_id: str, *, session: AsyncClientSession | None = None
    ) -> bool: ...
