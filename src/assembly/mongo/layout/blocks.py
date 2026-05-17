from dishka import Provider, Scope, provide

from src.domain.protocols.repositories import (
    LayoutBlockMessageRepositoryProtocol,
    LayoutBlockSingleRepositoryProtocol,
    LayoutBlockTableRepositoryProtocol,
)
from src.infra.mongo.documents import (
    LayoutBlockMessageDocument,
    LayoutBlockSingleDocument,
    LayoutBlockTableDocument,
)
from src.infra.mongo.protocols import ConverterProtocol
from src.infra.mongo.repositories import (
    LayoutBlockMessageRepository,
    LayoutBlockSingleRepository,
    LayoutBlockTableRepository,
)


class _BlocksProvider(Provider):
    @provide(scope=Scope.APP)
    async def __single(
        self, converter: ConverterProtocol
    ) -> LayoutBlockSingleRepositoryProtocol:
        return LayoutBlockSingleRepository(
            LayoutBlockSingleDocument, converter=converter
        )

    @provide(scope=Scope.APP)
    async def __table(
        self, converter: ConverterProtocol
    ) -> LayoutBlockTableRepositoryProtocol:
        return LayoutBlockTableRepository(
            LayoutBlockTableDocument, converter=converter
        )

    @provide(scope=Scope.APP)
    async def __message(
        self, converter: ConverterProtocol
    ) -> LayoutBlockMessageRepositoryProtocol:
        return LayoutBlockMessageRepository(
            LayoutBlockMessageDocument, converter=converter
        )
