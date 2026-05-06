from collections.abc import Callable, Mapping, Sequence
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from beanie import Document, UnionDoc, View
    from pymongo.monitoring import (
        CommandListener,
        ConnectionPoolListener,
        ServerHeartbeatListener,
        ServerListener,
        TopologyListener,
    )
    from pymongo.server_description import ServerDescription


type CollectedDocumentsType = Sequence[type[Document | UnionDoc | View]]
type QueryConditionsType = Sequence[Mapping[Any, Any] | bool]
type ServerSelectorType = (
    Callable[[list[ServerDescription]], list[ServerDescription]] | None
)
type EventListenerType = Sequence[
    CommandListener
    | ConnectionPoolListener
    | ServerHeartbeatListener
    | TopologyListener
    | ServerListener
]
