from collections.abc import Iterable
from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from pydantic import BaseModel
    from pymongo.asynchronous.client_session import AsyncClientSession


class AddMixinProtocol(Protocol):
    async def add[ReturnSchema, CreateSchema: BaseModel](
        self,
        condition: CreateSchema,
        *,
        session: AsyncClientSession | None = None,
        return_as: type[ReturnSchema],
    ) -> ReturnSchema: ...


class BulkAddWithReturnIdMixinProtocol(Protocol):
    async def bulk_add_with_return_id[CreateSchema: BaseModel](
        self,
        conditions: Iterable[CreateSchema],
        *,
        session: AsyncClientSession | None = None,
    ) -> list[str]: ...


class BulkAddMixinProtocol(Protocol):
    async def bulk_add[ReturnSchema, CreateSchema: BaseModel](
        self,
        conditions: Iterable[CreateSchema],
        *,
        session: AsyncClientSession | None = None,
        return_as: type[ReturnSchema],
        max_concurrent: int = 10,
    ) -> list[ReturnSchema]: ...
