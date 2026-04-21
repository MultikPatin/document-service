from typing import Protocol


class ExistsMixinProtocol(Protocol):
    async def exists[S](self, document_id: str, *, session: S) -> bool: ...


class CountMixinProtocol(Protocol):
    async def count[S](self, document_id: str, *, session: S) -> int: ...


class IncRefCountMixinProtocol(Protocol):
    async def inc_ref[S](self, document_id: str, *, session: S) -> bool: ...


class DecRefCountMixinProtocol(Protocol):
    async def dec_ref[S](self, document_id: str, *, session: S) -> bool: ...
