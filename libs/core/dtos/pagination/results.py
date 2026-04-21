from collections.abc import Sequence

from pydantic import BaseModel, Field


class BaseResult[T](BaseModel):
    items: Sequence[T]
    total: int | None = Field(default=None)


class PagesResultDTO[T](BaseResult[T]):
    current_page: int | None = Field(default=None)
    previous_page: int | None = Field(default=None)
    next_page: int | None = Field(default=None)


class LimitOffsetResultDTO[T](BaseResult[T]):
    limit: int | None = Field(ge=1)
    offset: int | None = Field(ge=0)


class CursorResultDTO[T](BaseResult[T]):
    current_page: str | None = Field(default=None)
    previous_page: str | None = Field(default=None)
    next_page: str | None = Field(default=None)
