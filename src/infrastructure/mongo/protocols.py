from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from pymongo.asynchronous.client_session import AsyncClientSession

    from src.infrastructure.mongo.annotations import ClientKwargsType


class TransactionRepositoryProtocol(Protocol):
    def start_session(self) -> AsyncClientSession: ...
    def set_session(self, session: AsyncClientSession | None) -> None: ...


class SettingsProtocol(Protocol):
    @property
    def database(self) -> str: ...
    @property
    def connection_string(self) -> str: ...
    @property
    def client_kwargs(self) -> ClientKwargsType: ...
