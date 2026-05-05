from pydantic import BaseModel, ConfigDict, Field, NonNegativeInt, PositiveInt

from src.domain.constants import CURSOR_PREVIOUS_PREFIX


class _Params(BaseModel):
    model_config = ConfigDict(frozen=True)


class PagesParams(_Params):
    number: PositiveInt = Field(default=1)
    size: PositiveInt = Field(default=50, le=100)

    @property
    def limit(self) -> int:
        return self.size

    @property
    def offset(self) -> int:
        return (self.number - 1) * self.size


class LimitOffsetParams(_Params):
    limit: PositiveInt = Field(default=50, le=100)
    offset: NonNegativeInt = Field(default=0)


class CursorParams(_Params):
    cursor: str | None = Field(default=None, min_length=1)
    size: PositiveInt = Field(default=50, le=100)

    @property
    def is_previous_cursor(self) -> bool:
        return (
            self.cursor.startswith(CURSOR_PREVIOUS_PREFIX)
            if self.cursor
            else False
        )
