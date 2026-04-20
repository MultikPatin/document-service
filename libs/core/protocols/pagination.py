from typing import Protocol


class PagesParamsProtocol(Protocol):
    number: int
    size: int


class LimitOffsetParamsProtocol(Protocol):
    limit: int
    offset: int


class CursorParamsProtocol(Protocol):
    cursor: str | None
    size: int
