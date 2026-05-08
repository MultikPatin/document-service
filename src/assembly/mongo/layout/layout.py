from dishka import Scope, provide

from src.domain.protocols.repositories import LayoutRepositoryProtocol
from src.infrastructure.mongo.documents import LayoutDocument
from src.infrastructure.mongo.protocols import ConverterProtocol
from src.infrastructure.mongo.repositories import LayoutRepository

from .blocks import _BlocksProvider
from .layers import _LayersProvider


class LayoutProvider(_LayersProvider, _BlocksProvider):
    @provide(scope=Scope.APP)
    async def __layout(
        self, converter: ConverterProtocol
    ) -> LayoutRepositoryProtocol:
        return LayoutRepository(LayoutDocument, converter=converter)
