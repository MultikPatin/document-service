from dishka import Provider, Scope, provide

from src.domain.protocols.repositories import (
    ReportSingleRepositoryProtocol,
    ReportTableRepositoryProtocol,
)
from src.infrastructure.mongo.documents import (
    ReportBlockSingleDocument,
    ReportBlockTableDocument,
)
from src.infrastructure.mongo.repositories import (
    ReportBlockSingleRepository,
    ReportBlockTableRepository,
)


class _BlocksProvider(Provider):
    @provide(scope=Scope.APP)
    async def __single(self) -> ReportSingleRepositoryProtocol:
        return ReportBlockSingleRepository(ReportBlockSingleDocument)

    @provide(scope=Scope.APP)
    async def __table(self) -> ReportTableRepositoryProtocol:
        return ReportBlockTableRepository(ReportBlockTableDocument)
