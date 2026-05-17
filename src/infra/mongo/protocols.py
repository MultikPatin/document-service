from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from collections.abc import Iterable

    from beanie import PydanticObjectId
    from pydantic import BaseModel
    from pymongo.asynchronous.client_session import AsyncClientSession

    from src.infra.mongo.annotations import ClientKwargsType


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


class ConverterProtocol(Protocol):
    @staticmethod
    def as_id(id_: str) -> PydanticObjectId: ...
    def as_ids(self, ids: Iterable[str]) -> Iterable[PydanticObjectId]: ...
    @staticmethod
    def as_dto[D: BaseModel, R](
        document: D, return_as: type[R], *, replace_links: bool = False
    ) -> R: ...
    def as_dtos[D: BaseModel, R](
        self,
        documents: Iterable[D],
        return_as: type[R],
        *,
        replace_links: bool = False,
    ) -> list[R]: ...
