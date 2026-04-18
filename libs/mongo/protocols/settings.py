from typing import Any, Protocol


class SettingsProtocol(Protocol):
    @property
    def database(self) -> str: ...
    @property
    def connection_string(self) -> str: ...
    @property
    def client_kwargs(self) -> dict[str, Any]: ...
