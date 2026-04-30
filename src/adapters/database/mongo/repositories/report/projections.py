from typing import Any

from beanie import Link
from bson import DBRef
from pydantic import BaseModel, Field, field_validator


class _LayoutIDProjection(BaseModel):
    layout: str = Field(min_length=1)

    @field_validator("layout", mode="before")
    @classmethod
    def convert_layout(cls, value: Any) -> str:  # noqa: ANN401
        if isinstance(value, DBRef):
            return str(value.id)
        if isinstance(value, Link):
            return str(value.ref.id)
        return str(value)
