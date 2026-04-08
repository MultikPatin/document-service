from collections.abc import Sequence
from typing import Any, Protocol


class SettingsProtocol(Protocol):
    @property
    def database(self) -> str: ...
    @property
    def client_kwargs(self) -> dict[str, Any]: ...
    def get_connections(self, with_secret: bool = False) -> Sequence[str]: ...
