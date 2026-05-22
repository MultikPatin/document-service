from dishka import Provider, Scope, provide

from src.domain.protocols.repositories import (
    LayoutLayerDefaultRepositoryProtocol,
    LayoutLayerSchemaRepositoryProtocol,
    LayoutLayerValidationRepositoryProtocol,
)
from src.infra.mongo.repositories.layout import layers


class Layers(Provider):
    @provide(scope=Scope.APP)
    async def __schema(self) -> LayoutLayerSchemaRepositoryProtocol:
        return layers.Shema()

    @provide(scope=Scope.APP)
    async def __validation(self) -> LayoutLayerValidationRepositoryProtocol:
        return layers.Validation()

    @provide(scope=Scope.APP)
    async def __default(self) -> LayoutLayerDefaultRepositoryProtocol:
        return layers.Default()
