from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from pymongo.asynchronous.client_session import AsyncClientSession


class ExistsMixinProtocol(Protocol):
    async def exists(
        self, document_id: str, *, session: AsyncClientSession | None = None
    ) -> bool: ...


class CountMixinProtocol(Protocol):
    async def count(
        self, document_id: str, *, session: AsyncClientSession | None = None
    ) -> int: ...


class IncRefCountMixinProtocol(Protocol):
    async def inc_ref(
        self, document_id: str, *, session: AsyncClientSession | None = None
    ) -> bool: ...


class DecRefCountMixinProtocol(Protocol):
    async def dec_ref(
        self, document_id: str, *, session: AsyncClientSession | None = None
    ) -> bool: ...
