from typing import Any

from beanie import Link
from bson import DBRef
from pydantic import BaseModel, field_validator


class LayoutIDProjection(BaseModel):
    layout: str

    @field_validator("layout", mode="before")
    @classmethod
    def convert_layout(cls, value: Any) -> str:  # noqa: ANN401
        if isinstance(value, DBRef):
            return str(value.id)
        if isinstance(value, Link):
            return str(value.ref.id)
        return str(value)
