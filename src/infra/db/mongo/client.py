import inspect
import logging
from collections.abc import Callable, Mapping, Sequence
from typing import TYPE_CHECKING, Any

from beanie import init_beanie
from bson.codec_options import DatetimeConversion
from pymongo import AsyncMongoClient

from .constants import LoggerNames

if TYPE_CHECKING:
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
    from .protocols import SettingsProtocol

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

logger = logging.getLogger(LoggerNames.init())


class Client:
    def __init__(  # noqa: PLR0913
        self,
        settings: SettingsProtocol,
        *,
        tz_aware: bool = False,
        datetime_conversion: DatetimeConversion = DatetimeConversion.DATETIME,
        document_class: DocumentClassType = None,
        type_registry: TypeRegistryType = None,
        server_selector: ServerSelectorType = None,
        driver: DriverType = None,
        event_listeners: EventListenerType = None,
        auto_encryption_opts: AutoEncryptionOptsType = None,
        server_api: ServerApiType = None,
    ) -> None:
        if event_listeners is None:
            event_listeners = ()

        self._database = settings.database
        logger.info("client initialization...")
        self._client = AsyncMongoClient(
            host=settings.get_connections(with_secret=True),
            tz_aware=tz_aware,
            datetime_conversion=datetime_conversion,
            document_class=document_class,
            type_registry=type_registry,
            server_selector=server_selector,
            driver=driver,
            event_listeners=event_listeners,
            auto_encryption_opts=auto_encryption_opts,
            server_api=server_api,
            **settings.client_kwargs,
        )
        logger.info("client initialization completed successfully")

    async def init_beanie(
        self,
        documents: CollectedDocumentsType,
        *,
        allow_index_dropping: bool = False,
        recreate_views: bool = False,
        skip_indexes: bool = False,
    ) -> None:
        logger.info("beanie initialization...")

        excluded = ("self", "documents")
        if logger.getEffectiveLevel() <= logging.DEBUG:
            frame = inspect.currentframe()
            if frame:
                args, _, _, values = inspect.getargvalues(frame)
                params = {a: values[a] for a in args if a not in excluded}
                logger.debug("params: %s", params)
                del frame

        await init_beanie(
            database=self.database,
            document_models=documents,
            allow_index_dropping=allow_index_dropping,
            recreate_views=recreate_views,
            skip_indexes=skip_indexes,
        )
        logger.info("beanie initialization completed successfully")

    async def close(self) -> None:
        logger.info("stopping the client...")
        await self._client.aclose()
        logger.info("stopping the client has been completed successfully")

    def start_session(self) -> AsyncClientSession:
        return self._client.start_session()

    @property
    def client(self) -> AsyncMongoClient:
        return self._client

    @property
    def database(self) -> AsyncDatabase:
        return self._client[self._database]

    def collection(self, name: str, /) -> AsyncCollection:
        return self.database[name]

    @property
    async def collections(self) -> list[str]:
        return await self.database.list_collection_names()

    async def drop_database(self) -> None:
        logger.info("dropping database '%s'...", self._database)
        await self._client.drop_database(self._database)
        logger.info(
            "database '%s' has been dropped successfully", self._database
        )

    async def drop_collection(self, name: str, /) -> None:
        logger.info("dropping collection '%s'...", name)
        collection = self.collection(name)
        await collection.drop()
        logger.info("collection '%s' has been dropped successfully", name)
