from datetime import datetime
from typing import Any

from beanie import Link
from bson import DBRef
from pydantic import BaseModel, Field, field_validator


class IDProjection(BaseModel):
    id: str = Field(validation_alias="_id")

    @field_validator("id", mode="before")
    @classmethod
    def convert_id(cls, value: Any) -> str:  # noqa: ANN401
        if isinstance(value, str):
            return value
        return str(value)


class PaginatedLayoutProjection(IDProjection):
    label: str

    created_at: datetime
    updated_at: datetime | None


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
