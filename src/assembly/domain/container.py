from typing import TYPE_CHECKING

from dishka import make_async_container

from src.assembly.mongo import MongoProvider

from .composite import DomainProvider

if TYPE_CHECKING:
    from dishka import AsyncContainer, Provider


def make_container(
    scope_provider: Provider | None = None,
) -> AsyncContainer:
    providers: list[Provider] = [
        DomainProvider(),
        MongoProvider(),
    ]
    if scope_provider is not None:
        providers.append(scope_provider)
    return make_async_container(*providers)
