from dishka import Provider, Scope, provide

from src.domain.protocols.repositories import (
    LayoutLayerDefaultRepositoryProtocol,
    LayoutLayerSchemaRepositoryProtocol,
    LayoutLayerValidationRepositoryProtocol,
)
from src.infrastructure.mongo.documents import (
    LayoutLayerDefaultDocument,
    LayoutLayerSchemaDocument,
    LayoutLayerValidationDocument,
)
from src.infrastructure.mongo.protocols import ConverterProtocol
from src.infrastructure.mongo.repositories import (
    LayoutLayerDefaultRepository,
    LayoutLayerSchemaRepository,
    LayoutLayerValidationRepository,
)


class _LayersProvider(Provider):
    @provide(scope=Scope.APP)
    async def __schema(
        self, converter: ConverterProtocol
    ) -> LayoutLayerSchemaRepositoryProtocol:
        return LayoutLayerSchemaRepository(
            LayoutLayerSchemaDocument, converter=converter
        )

    @provide(scope=Scope.APP)
    async def __validation(
        self, converter: ConverterProtocol
    ) -> LayoutLayerValidationRepositoryProtocol:
        return LayoutLayerValidationRepository(
            LayoutLayerValidationDocument, converter=converter
        )

    @provide(scope=Scope.APP)
    async def __default(
        self, converter: ConverterProtocol
    ) -> LayoutLayerDefaultRepositoryProtocol:
        return LayoutLayerDefaultRepository(
            LayoutLayerDefaultDocument, converter=converter
        )
