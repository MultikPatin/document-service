from dishka import Scope, provide

from src.domain.protocols.repositories import ReportRepositoryProtocol
from src.infra.mongo.documents import ReportDocument
from src.infra.mongo.protocols import ConverterProtocol
from src.infra.mongo.repositories import ReportRepository

from .blocks import _BlocksProvider


class ReportProvider(_BlocksProvider):
    @provide(scope=Scope.APP)
    async def __report(
        self, converter: ConverterProtocol
    ) -> ReportRepositoryProtocol:
        return ReportRepository(ReportDocument, converter=converter)
