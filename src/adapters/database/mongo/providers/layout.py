from dishka import Provider, Scope, provide

from src.adapters.database.mongo.documents import (
    LayoutBlockMessageDocument,
    LayoutBlockSingleDocument,
    LayoutBlockTableDocument,
    LayoutDocument,
    LayoutLayerDefaultDocument,
    LayoutLayerSchemaDocument,
    LayoutLayerValidationDocument,
)
from src.adapters.database.mongo.repositories import (
    LayoutBlockMessageRepository,
    LayoutBlockSingleRepository,
    LayoutBlockTableRepository,
    LayoutLayerDefaultRepository,
    LayoutLayerSchemaRepository,
    LayoutLayerValidationRepository,
    LayoutRepository,
)
from src.application.protocols.repositories import (
    LayoutBlockMessageRepositoryProtocol,
    LayoutBlockSingleRepositoryProtocol,
    LayoutBlockTableRepositoryProtocol,
    LayoutLayerDefaultRepositoryProtocol,
    LayoutLayerSchemaRepositoryProtocol,
    LayoutLayerValidationRepositoryProtocol,
    LayoutRepositoryProtocol,
)


class LayoutProvider(Provider):
    @provide(scope=Scope.APP)
    async def __layout(self) -> LayoutRepositoryProtocol:
        return LayoutRepository(LayoutDocument)


class LayoutBlcokProvider(Provider):
    @provide(scope=Scope.APP)
    async def __single(self) -> LayoutBlockSingleRepositoryProtocol:
        return LayoutBlockSingleRepository(LayoutBlockSingleDocument)

    @provide(scope=Scope.APP)
    async def __table(self) -> LayoutBlockTableRepositoryProtocol:
        return LayoutBlockTableRepository(LayoutBlockTableDocument)

    @provide(scope=Scope.APP)
    async def __message(self) -> LayoutBlockMessageRepositoryProtocol:
        return LayoutBlockMessageRepository(LayoutBlockMessageDocument)


class LayoutLayerProvider(Provider):
    @provide(scope=Scope.APP)
    async def __schema(self) -> LayoutLayerSchemaRepositoryProtocol:
        return LayoutLayerSchemaRepository(LayoutLayerSchemaDocument)

    @provide(scope=Scope.APP)
    async def __validation(self) -> LayoutLayerValidationRepositoryProtocol:
        return LayoutLayerValidationRepository(LayoutLayerValidationDocument)

    @provide(scope=Scope.APP)
    async def __default(self) -> LayoutLayerDefaultRepositoryProtocol:
        return LayoutLayerDefaultRepository(LayoutLayerDefaultDocument)
