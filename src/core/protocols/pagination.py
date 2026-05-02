from typing import Protocol


class PagesParamsProtocol(Protocol):
    number: int
    size: int

    @property
    def limit(self) -> int: ...
    @property
    def offset(self) -> int: ...


class LimitOffsetParamsProtocol(Protocol):
    limit: int
    offset: int


class CursorParamsProtocol(Protocol):
    cursor: str | None
    size: int

    def is_previous_cursor(self) -> bool: ...
