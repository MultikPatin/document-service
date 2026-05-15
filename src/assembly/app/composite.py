from typing import Annotated

from dishka import FromComponent, Provider, Scope, provide

from src.assembly.enums import ComponentsEnum
from src.assembly.protocols import InitComponentProtocol, InitComponentsProtocol

database = ComponentsEnum.mongo


class ApplicationProvider(Provider):
    @provide(scope=Scope.APP)
    async def __init(
        self,
        mongo: Annotated[InitComponentProtocol, FromComponent(database)],
    ) -> InitComponentsProtocol:
        return InitComponentsProtocol
