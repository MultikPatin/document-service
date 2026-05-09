from typing import Protocol


class ExistsMixinProtocol(Protocol):
    async def exists(self, id_: str) -> bool: ...


class CountMixinProtocol(Protocol):
    async def count(self, id_: str) -> int: ...
