from dishka import Provider, Scope, provide

from src.domain.protocols.repositories import (
    LayoutBlockMessageRepositoryProtocol,
    LayoutBlockSingleRepositoryProtocol,
    LayoutBlockTableRepositoryProtocol,
)
from src.infrastructure.mongo.documents import (
    LayoutBlockMessageDocument,
    LayoutBlockSingleDocument,
    LayoutBlockTableDocument,
)
from src.infrastructure.mongo.repositories import (
    LayoutBlockMessageRepository,
    LayoutBlockSingleRepository,
    LayoutBlockTableRepository,
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
