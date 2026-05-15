from dishka import Provider, Scope, provide

from src.domain.protocols.repositories import (
    ReportSingleRepositoryProtocol,
    ReportTableRepositoryProtocol,
)
from src.infra.mongo.documents import (
    ReportBlockSingleDocument,
    ReportBlockTableDocument,
)
from src.infra.mongo.protocols import ConverterProtocol
from src.infra.mongo.repositories import (
    ReportBlockSingleRepository,
    ReportBlockTableRepository,
)


class _BlocksProvider(Provider):
    @provide(scope=Scope.APP)
    async def __single(
        self, converter: ConverterProtocol
    ) -> ReportSingleRepositoryProtocol:
        return ReportBlockSingleRepository(
            ReportBlockSingleDocument, converter=converter
        )

    @provide(scope=Scope.APP)
    async def __table(
        self, converter: ConverterProtocol
    ) -> ReportTableRepositoryProtocol:
        return ReportBlockTableRepository(
            ReportBlockTableDocument, converter=converter
        )
