from collections.abc import Set
from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from pymongo.asynchronous.client_session import AsyncClientSession


class GetMixinProtocol(Protocol):
    async def get[ReturnSchema](
        self,
        document_id: str,
        *,
        session: AsyncClientSession | None = None,
        return_as: type[ReturnSchema],
    ) -> ReturnSchema | None: ...


class GetByHashMixinProtocol(Protocol):
    async def get_by_hash[ReturnSchema](
        self,
        hash_string: str,
        *,
        session: AsyncClientSession | None = None,
        return_as: type[ReturnSchema],
    ) -> ReturnSchema | None: ...


class GetByIDsMixinProtocol(Protocol):
    async def get_by_ids[ReturnSchema](
        self,
        document_ids: Set[str],
        *,
        session: AsyncClientSession | None = None,
        return_as: type[ReturnSchema],
        batch_size: int | None = None,
        max_concurrent: int = 10,
    ) -> list[ReturnSchema] | None: ...
