from dishka import Provider, Scope, provide

from src.adapters.database.mongo.documents import (
    ReportBlockSingleDocument,
    ReportBlockTableDocument,
    ReportDocument,
)
from src.adapters.database.mongo.repositories import (
    ReportBlockSingleRepository,
    ReportBlockTableRepository,
    ReportRepository,
)
from src.application.protocols.repositories import (
    ReportRepositoryProtocol,
    ReportSingleRepositoryProtocol,
    ReportTableRepositoryProtocol,
)


class ReportProvider(Provider):
    @provide(scope=Scope.APP)
    async def __input(self) -> ReportRepositoryProtocol:
        return ReportRepository(ReportDocument)


class ReportBlockProvider(Provider):
    @provide(scope=Scope.APP)
    async def __single(self) -> ReportSingleRepositoryProtocol:
        return ReportBlockSingleRepository(ReportBlockSingleDocument)

    @provide(scope=Scope.APP)
    async def __table(self) -> ReportTableRepositoryProtocol:
        return ReportBlockTableRepository(ReportBlockTableDocument)
