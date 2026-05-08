from collections.abc import Set
from typing import Protocol


class GetMixinProtocol(Protocol):
    async def get[R](self, id_: str, *, return_as: type[R]) -> R | None: ...


class GetByHashMixinProtocol(Protocol):
    async def get_by_hash[R](
        self, hash_string: str, *, return_as: type[R]
    ) -> R | None: ...


class GetByIDsMixinProtocol(Protocol):
    async def get_by_ids[R](
        self,
        ids: Set[str],
        *,
        return_as: type[R],
        batch_size: int | None = None,
        max_concurrent: int = 10,
    ) -> list[R] | None: ...
