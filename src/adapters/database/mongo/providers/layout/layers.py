from dishka import Provider, Scope, provide

from src.adapters.database.mongo.documents import (
    LayoutLayerDefaultDocument,
    LayoutLayerSchemaDocument,
    LayoutLayerValidationDocument,
)
from src.adapters.database.mongo.repositories import (
    LayoutLayerDefaultRepository,
    LayoutLayerSchemaRepository,
    LayoutLayerValidationRepository,
)
from src.application.protocols.repositories import (
    LayoutLayerDefaultRepositoryProtocol,
    LayoutLayerSchemaRepositoryProtocol,
    LayoutLayerValidationRepositoryProtocol,
)


class _LayersProvider(Provider):
    @provide(scope=Scope.APP)
    async def __schema(self) -> LayoutLayerSchemaRepositoryProtocol:
        return LayoutLayerSchemaRepository(LayoutLayerSchemaDocument)

    @provide(scope=Scope.APP)
    async def __validation(self) -> LayoutLayerValidationRepositoryProtocol:
        return LayoutLayerValidationRepository(LayoutLayerValidationDocument)

    @provide(scope=Scope.APP)
    async def __default(self) -> LayoutLayerDefaultRepositoryProtocol:
        return LayoutLayerDefaultRepository(LayoutLayerDefaultDocument)
