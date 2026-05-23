from dishka import Provider, Scope, provide

from src.domain.protocols.repositories import (
    LayoutBlockMessageRepositoryProtocol,
    LayoutBlockSingleRepositoryProtocol,
    LayoutBlockTableRepositoryProtocol,
)
from src.infra.mongo.repositories.layout import blocks


class Blocks(Provider):
    @provide(scope=Scope.APP)
    async def __single(self) -> LayoutBlockSingleRepositoryProtocol:
        return blocks.Single()

    @provide(scope=Scope.APP)
    async def __table(self) -> LayoutBlockTableRepositoryProtocol:
        return blocks.Table()

    @provide(scope=Scope.APP)
    async def __message(self) -> LayoutBlockMessageRepositoryProtocol:
        return blocks.Message()
