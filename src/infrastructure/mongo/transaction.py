from typing import TYPE_CHECKING, Self

from src.infrastructure.mongo.errors import StartSessionError

if TYPE_CHECKING:
    from pymongo.asynchronous.client_session import AsyncClientSession

    from src.infrastructure.mongo.protocols import TransactionRepositoryProtocol


class AsyncTransactionContext:
    def __init_(self, *repositories: TransactionRepositoryProtocol) -> None:
        self._repositories = repositories
        self._session: AsyncClientSession | None = None

    async def __aenter__(self) -> Self:
        for repo in self._repositories:
            self._session = repo.start_session()
            if self._session is not None:
                break
        if self._session is None:
            raise StartSessionError

        await self._session.start_transaction()

        for repo in self._repositories:
            repo.set_session(self._session)

        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:  # noqa: ANN001
        try:
            if exc_type is not None:
                if self._session:
                    await self._session.abort_transaction()
            elif self._session:
                await self._session.commit_transaction()
        finally:
            for repo in self._repositories:
                repo.set_session(None)
            if self._session:
                await self._session.end_session()
