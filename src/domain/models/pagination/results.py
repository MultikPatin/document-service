from collections.abc import Sequence
from typing import TYPE_CHECKING

from pydantic import BaseModel, ConfigDict

from src.domain.constants import CURSOR_PREVIOUS_PREFIX

if TYPE_CHECKING:
    from .params import CursorParams, LimitOffsetParams, PagesParams


class _ResultDTO[T](BaseModel):
    model_config = ConfigDict(frozen=True)

    items: Sequence[T]
    total: int


class PagesResult[T](_ResultDTO[T]):
    current_page: int
    previous_page: int | None
    next_page: int | None

    @classmethod
    def from_params(
        cls, params: PagesParams, count: int, items: Sequence[T]
    ) -> PagesResult[T]:
        pages = count // params.size
        if params.size * pages < count:
            pages += 1
        next_page = (
            params.number + 1 if pages > 1 and params.number < pages else None
        )
        previous_page = (
            params.number - 1 if pages > 1 and params.number > 1 else None
        )
        return cls(
            items=items,
            total=pages,
            current_page=params.number,
            previous_page=previous_page,
            next_page=next_page,
        )


class LimitOffsetResult[T](_ResultDTO[T]):
    limit: int
    offset: int

    @classmethod
    def from_params(
        cls, params: LimitOffsetParams, count: int, items: Sequence[T]
    ) -> LimitOffsetResult[T]:
        return cls(
            items=items,
            total=count,
            limit=params.limit,
            offset=params.offset,
        )


class CursorResult[T](_ResultDTO[T]):
    current_page: str | None
    previous_page: str | None
    next_page: str | None

    @classmethod
    def from_params(
        cls, params: CursorParams, count: int, items: Sequence[T]
    ) -> CursorResult[T]:
        if params.is_previous_cursor:
            items = list(reversed(items[: params.size]))

        if not hasattr(items[0], "id") or not hasattr(items[-1], "id"):
            msg = "The items return model must have an id attribute"
            raise AttributeError(msg)

        next_page = str(items[-1].id) if len(items) > params.size else None
        previous_page = f"{CURSOR_PREVIOUS_PREFIX}{items[0].id}"

        return cls(
            items=items,
            total=count,
            current_page=params.cursor,
            previous_page=previous_page,
            next_page=next_page,
        )
