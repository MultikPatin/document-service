from dishka import Scope, provide

from src.adapters.database.mongo.documents import LayoutDocument
from src.adapters.database.mongo.repositories import LayoutRepository
from src.domain.protocols.repositories import LayoutRepositoryProtocol

from .blocks import _BlocksProvider
from .layers import _LayersProvider


class LayoutProvider(_LayersProvider, _BlocksProvider):
    @provide(scope=Scope.APP)
    async def __layout(self) -> LayoutRepositoryProtocol:
        return LayoutRepository(LayoutDocument)
