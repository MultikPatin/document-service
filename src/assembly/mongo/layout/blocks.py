from dishka import Provider, Scope, provide

from src.adapters.database.mongo.documents import (
    LayoutBlockMessageDocument,
    LayoutBlockSingleDocument,
    LayoutBlockTableDocument,
)
from src.adapters.database.mongo.repositories import (
    LayoutBlockMessageRepository,
    LayoutBlockSingleRepository,
    LayoutBlockTableRepository,
)
from src.domain.protocols.repositories import (
    LayoutBlockMessageRepositoryProtocol,
    LayoutBlockSingleRepositoryProtocol,
    LayoutBlockTableRepositoryProtocol,
)


class _BlocksProvider(Provider):
    @provide(scope=Scope.APP)
    async def __single(self) -> LayoutBlockSingleRepositoryProtocol:
        return LayoutBlockSingleRepository(LayoutBlockSingleDocument)

    @provide(scope=Scope.APP)
    async def __table(self) -> LayoutBlockTableRepositoryProtocol:
        return LayoutBlockTableRepository(LayoutBlockTableDocument)

    @provide(scope=Scope.APP)
    async def __message(self) -> LayoutBlockMessageRepositoryProtocol:
        return LayoutBlockMessageRepository(LayoutBlockMessageDocument)
