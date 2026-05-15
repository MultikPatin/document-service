from collections.abc import Awaitable, Callable
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from fastapi import Request, Response


type CallNext = Callable[[Request], Awaitable[Response]]
