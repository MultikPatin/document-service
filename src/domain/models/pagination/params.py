from pydantic import BaseModel, Field, NonNegativeInt, PositiveInt

from src.domain.constants import CURSOR_PREVIOUS_PREFIX
from src.domain.utils import vo_model_config


class _Params(BaseModel):
    model_config = vo_model_config()


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
