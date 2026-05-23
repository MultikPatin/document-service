from dishka import Scope, provide

from src.domain.protocols.repositories import LayoutRepositoryProtocol
from src.infra.mongo.repositories.layout import Layout as LayoutRepository

from .blocks import Blocks
from .layers import Layers


class Layout(Layers, Blocks):
    @provide(scope=Scope.APP)
    async def __layout(self) -> LayoutRepositoryProtocol:
        return LayoutRepository()
