from collections.abc import Iterable
from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from pydantic import BaseModel


class AddMixinProtocol(Protocol):
    async def add[R, S, C: BaseModel](
        self, condition: C, *, session: S, return_as: type[R]
    ) -> R: ...


class BulkAddWithReturnIdMixinProtocol(Protocol):
    async def bulk_add_with_return_id[S, C: BaseModel](
        self, conditions: Iterable[C], *, session: S
    ) -> list[str]: ...


class BulkAddMixinProtocol(Protocol):
    async def bulk_add[R, S, C: BaseModel](
        self,
        conditions: Iterable[C],
        *,
        session: S,
        return_as: type[R],
        max_concurrent: int = 10,
    ) -> list[R]: ...
