from dishka import Provider, Scope, provide

from src.adapters.database.mongo.documents import (
    ReportBlockSingleDocument,
    ReportBlockTableDocument,
)
from src.adapters.database.mongo.repositories import (
    ReportBlockSingleRepository,
    ReportBlockTableRepository,
)
from src.application.protocols.repositories import (
    ReportSingleRepositoryProtocol,
    ReportTableRepositoryProtocol,
)


class _BlocksProvider(Provider):
    @provide(scope=Scope.APP)
    async def __single(self) -> ReportSingleRepositoryProtocol:
        return ReportBlockSingleRepository(ReportBlockSingleDocument)

    @provide(scope=Scope.APP)
    async def __table(self) -> ReportTableRepositoryProtocol:
        return ReportBlockTableRepository(ReportBlockTableDocument)
