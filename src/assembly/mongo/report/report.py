from dishka import Scope, provide

from src.adapters.database.mongo.documents import ReportDocument
from src.adapters.database.mongo.repositories import ReportRepository
from src.domain.protocols.repositories import ReportRepositoryProtocol

from .blocks import _BlocksProvider


class ReportProvider(_BlocksProvider):
    @provide(scope=Scope.APP)
    async def __input(self) -> ReportRepositoryProtocol:
        return ReportRepository(ReportDocument)
