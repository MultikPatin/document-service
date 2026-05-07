from dishka import Scope, provide

from src.domain.protocols.repositories import ReportRepositoryProtocol
from src.infrastructure.mongo.documents import ReportDocument
from src.infrastructure.mongo.repositories import ReportRepository

from .blocks import _BlocksProvider


class ReportProvider(_BlocksProvider):
    @provide(scope=Scope.APP)
    async def __input(self) -> ReportRepositoryProtocol:
        return ReportRepository(ReportDocument)
