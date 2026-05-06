from collections.abc import Sequence
from typing import TYPE_CHECKING

from pydantic import BaseModel, ConfigDict, Field, NonNegativeInt, PositiveInt

from src.domain.constants import CURSOR_PREVIOUS_PREFIX

if TYPE_CHECKING:
    from src.core.protocols.pagination import (
        CursorParamsProtocol,
        LimitOffsetParamsProtocol,
        PagesParamsProtocol,
    )


class _ResultDTO[T](BaseModel):
    model_config = ConfigDict(frozen=True)

    items: Sequence[T]
    total: NonNegativeInt


class PagesResultDTO[T](_ResultDTO[T]):
    current_page: PositiveInt | None
    previous_page: PositiveInt | None = Field(default=None)
    next_page: PositiveInt | None = Field(default=None)

    @classmethod
    def from_params(
        cls, params: PagesParamsProtocol, count: int, items: Sequence[T]
    ) -> PagesResultDTO[T]:
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


class LimitOffsetResultDTO[T](_ResultDTO[T]):
    limit: PositiveInt | None
    offset: NonNegativeInt | None

    @classmethod
    def from_params(
        cls, params: LimitOffsetParamsProtocol, count: int, items: Sequence[T]
    ) -> LimitOffsetResultDTO[T]:
        return cls(
            items=items,
            total=count,
            limit=params.limit,
            offset=params.offset,
        )


class CursorResultDTO[T](_ResultDTO[T]):
    current_page: str | None = Field(default=None)
    previous_page: str | None = Field(default=None)
    next_page: str | None = Field(default=None)

    @classmethod
    def from_params(
        cls, params: CursorParamsProtocol, count: int, items: Sequence[T]
    ) -> CursorResultDTO[T]:
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
