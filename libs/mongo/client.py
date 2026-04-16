import inspect
import logging
from collections.abc import Callable, Mapping, Sequence
from typing import TYPE_CHECKING, Any

from beanie import init_beanie
from bson.codec_options import DatetimeConversion
from pymongo import AsyncMongoClient

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

    from src.adapters.database.mongo.documents import (
        CollectedDocumentsType,
    )

    from .protocols import SettingsProtocol

type ServerSelectorType = (
    Callable[[list[ServerDescription]], list[ServerDescription]] | None
)
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


class Client:
    def __init__(  # noqa: PLR0913
        self,
        settings: SettingsProtocol,
        logger: logging.Logger,
        *,
        tz_aware: bool = False,
        datetime_conversion: DatetimeConversion = DatetimeConversion.DATETIME,
        document_class: type[Mapping[str, Any]] | None = None,
        type_registry: TypeRegistry | None = None,
        server_selector: ServerSelectorType = None,
        driver: DriverInfo | None = None,
        event_listeners: EventListenerType = None,
        auto_encryption_opts: AutoEncryptionOpts | None = None,
        server_api: ServerApi | None = None,
    ) -> None:
        if event_listeners is None:
            event_listeners = ()

        self._database = settings.database
        self._logger = logger
        self._logger.info("client initialization...")
        self._client = AsyncMongoClient(
            host=settings.connection_string,
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
        self._logger.info("client initialization completed successfully")

    async def init_beanie(
        self,
        documents: CollectedDocumentsType,
        *,
        allow_index_dropping: bool = False,
        recreate_views: bool = False,
        skip_indexes: bool = False,
    ) -> None:
        self._logger.info("beanie initialization...")

        excluded = ("self", "documents")
        if self._is_debug_logger_level():
            frame = inspect.currentframe()
            if frame:
                args, _, _, values = inspect.getargvalues(frame)
                params = {a: values[a] for a in args if a not in excluded}
                self._logger.debug("params: %s", params)
                del frame

        await init_beanie(
            database=self.database,
            document_models=documents,
            allow_index_dropping=allow_index_dropping,
            recreate_views=recreate_views,
            skip_indexes=skip_indexes,
        )
        self._logger.info("beanie initialization completed successfully")

    async def close(self) -> None:
        self._logger.info("stopping the client...")
        await self._client.aclose()
        self._logger.info("stopping the client has been completed successfully")

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
        self._logger.info("dropping database '%s'...", self._database)
        await self._client.drop_database(self._database)
        self._logger.info(
            "database '%s' has been dropped successfully", self._database
        )

    async def drop_collection(self, name: str, /) -> None:
        self._logger.info("dropping collection '%s'...", name)
        collection = self.collection(name)
        await collection.drop()
        self._logger.info("collection '%s' has been dropped successfully", name)

    def _is_debug_logger_level(self) -> bool:
        return self._logger.getEffectiveLevel() <= logging.DEBUG
