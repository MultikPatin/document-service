from typing import TYPE_CHECKING, Any, Literal

from beanie import init_beanie
from pymongo import AsyncMongoClient

if TYPE_CHECKING:
    from collections.abc import Callable, Mapping, Sequence

    from bson.codec_options import TypeRegistry
    from pymongo.asynchronous.client_session import AsyncClientSession
    from pymongo.asynchronous.collection import AsyncCollection
    from pymongo.asynchronous.database import AsyncDatabase
    from pymongo.driver_info import DriverInfo
    from pymongo.encryption_options import AutoEncryptionOpts
    from pymongo.monitoring import (
        CommandListener,
        ConnectionPoolListener,
        ServerHeartbeatListener,
        ServerListener,
        TopologyListener,
    )
    from pymongo.server_api import ServerApi
    from pymongo.server_description import ServerDescription

    from .docs import CollectedDocumentsType
    from .settings import _Settings

type DatetimeConversionType = Literal[
    "datetime_ms", "datetime", "datetime_auto", "datetime_clamp"
]
type DocumentClassType = type[Mapping[str, Any]] | None
type TypeRegistryType = TypeRegistry | None
type ServerSelectorType = (
    Callable[[list[ServerDescription]], list[ServerDescription]] | None
)
type DriverType = DriverInfo | None
type EventListenerType = (
    Sequence[
        CommandListener
        | ConnectionPoolListener
        | ServerHeartbeatListener
        | TopologyListener
        | ServerListener
    ]
    | None
)
type AutoEncryptionOptsType = AutoEncryptionOpts | None
type ServerApiType = ServerApi | None


class _Client:
    def __init__(  # noqa: PLR0913
        self,
        settings: _Settings,
        tz_aware: bool = False,
        datetime_conversion: DatetimeConversionType = "datetime",
        document_class: DocumentClassType = None,
        type_registry: TypeRegistryType = None,
        server_selector: ServerSelectorType = None,
        driver: DriverType = None,
        event_listeners: EventListenerType = None,
        auto_encryption_opts: AutoEncryptionOptsType = None,
        server_api: ServerApiType = None,
    ) -> None:
        self._database = settings.DATABASE
        self._client = AsyncMongoClient(
            host=settings.dsn.unicode_string(),
            tz_aware=tz_aware,
            datetime_conversion=datetime_conversion,
            document_class=document_class,
            type_registry=type_registry,
            server_selector=server_selector,
            driver=driver,
            event_listeners=event_listeners,
            auto_encryption_opts=auto_encryption_opts,
            server_api=server_api,
            **settings.get_client_kwargs(),
        )

    async def init(self, documents: CollectedDocumentsType) -> None:
        await init_beanie(database=self.database, document_models=documents)

    async def close(self) -> None:
        await self._client.aclose()

    def start_session(self) -> AsyncClientSession:
        return self._client.start_session()

    @property
    def client(self) -> AsyncMongoClient:
        return self._client

    @property
    def database(self) -> AsyncDatabase:
        return self._client[self._database]

    def collection(self, name: str) -> AsyncCollection:
        return self.database[name]

    @property
    async def collections(self) -> list[str]:
        return await self.database.list_collection_names()

    async def drop_database(self) -> None:
        await self._client.drop_database(self._database)

    async def drop_collection(self, name: str) -> None:
        collection = self.collection(name)
        await collection.drop()
