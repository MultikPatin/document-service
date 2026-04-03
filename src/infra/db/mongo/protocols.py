from collections.abc import Sequence
from typing import Any, Protocol


class SettingsProtocol(Protocol):
    @property
    def database(self) -> str: ...
    @property
    def client_kwargs(self) -> dict[str, Any]: ...
    @property
    def connections(self) -> str | Sequence[str]: ...
