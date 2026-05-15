from typing import Any, Protocol


class InitComponentsProtocol(Protocol): ...


class InitComponentProtocol(Protocol): ...


class ApiBuilderProtocol(Protocol):
    def build(self) -> Any: ...  # noqa: ANN401
