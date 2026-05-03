from collections.abc import Set
from typing import Protocol


class GetMixinProtocol(Protocol):
    async def get[R, S](
        self, document_id: str, *, session: S, return_as: type[R]
    ) -> R | None: ...


class GetByHashMixinProtocol(Protocol):
    async def get_by_hash[R, S](
        self, hash_string: str, *, session: S, return_as: type[R]
    ) -> R | None: ...


class GetByIDsMixinProtocol(Protocol):
    async def get_by_ids[R, S](
        self,
        document_ids: Set[str],
        *,
        session: S,
        return_as: type[R],
        batch_size: int | None = None,
        max_concurrent: int = 10,
    ) -> list[R] | None: ...
