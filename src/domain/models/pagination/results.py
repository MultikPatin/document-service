from collections.abc import Sequence
from typing import TYPE_CHECKING

from pydantic import BaseModel

from src.domain.constants import CURSOR_PREVIOUS_PREFIX
from src.domain.entities import BaseEntity
from src.domain.utils import vo_model_config

if TYPE_CHECKING:
    from src.domain.protocols.pagination import (
        CursorParamsProtocol,
        LimitOffsetParamsProtocol,
        PagesParamsProtocol,
    )


class _Result[T](BaseModel):
    model_config = vo_model_config()

    items: Sequence[T]
    total: int


class PagesResult[T](_Result):
    current_page: int
    previous_page: int | None
    next_page: int | None

    @classmethod
    def from_params(
        cls, params: PagesParamsProtocol, count: int, items: Sequence[T]
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


class LimitOffsetResult[T](_Result):
    limit: int
    offset: int

    @classmethod
    def from_params(
        cls, params: LimitOffsetParamsProtocol, count: int, items: Sequence[T]
    ) -> LimitOffsetResult[T]:
        return cls(
            items=items,
            total=count,
            limit=params.limit,
            offset=params.offset,
        )


class CursorResult[T: BaseEntity](_Result):
    current_page: str | None
    previous_page: str | None
    next_page: str | None

    @classmethod
    def from_params(
        cls, params: CursorParamsProtocol, count: int, items: Sequence[T]
    ) -> CursorResult[T]:
        if params.is_previous_cursor:
            items = list(reversed(items[: params.size]))

        next_page = str(items[-1].id) if len(items) > params.size else None
        previous_page = f"{CURSOR_PREVIOUS_PREFIX}{items[0].id}"

        return cls(
            items=items,
            total=count,
            current_page=params.cursor,
            previous_page=previous_page,
            next_page=next_page,
        )
