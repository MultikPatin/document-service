from typing import TYPE_CHECKING, Protocol

from libs.mongo.protocols.repository_methods import (
    AddMixinProtocol,
    BulkAddMixinProtocol,
    GetMixinProtocol,
)

if TYPE_CHECKING:
    from pydantic import BaseModel
    from pymongo.asynchronous.client_session import AsyncClientSession


class ReportRepositoryProtocol(GetMixinProtocol, AddMixinProtocol, Protocol):
    async def get_full_links[ReturnSchema: BaseModel](
        self,
        document_id: str,
        *,
        session: AsyncClientSession,
        return_as: type[ReturnSchema],
    ) -> ReturnSchema | None: ...
    async def get_layout_id(
        self, document_id: str, *, session: AsyncClientSession
    ) -> str | None: ...


class ReportSingleRepositoryProtocol(BulkAddMixinProtocol, Protocol): ...


class ReportTableRepositoryProtocol(BulkAddMixinProtocol, Protocol): ...
