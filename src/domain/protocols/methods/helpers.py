from typing import Protocol


class ExistsMixinProtocol(Protocol):
    async def exists[S](self, id_: str) -> bool: ...


class CountMixinProtocol(Protocol):
    async def count[S](self, id_: str) -> int: ...


class IncRefCountMixinProtocol(Protocol):
    async def inc_ref[S](self, id_: str) -> bool: ...


class DecRefCountMixinProtocol(Protocol):
    async def dec_ref[S](self, id_: str) -> bool: ...
