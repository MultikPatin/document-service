from typing import Any

from pydantic import BaseModel, Field, field_validator


class ID(BaseModel):
    id: str = Field(min_length=1)

    @field_validator("id", mode="before")
    @classmethod
    def convert_id(cls, value: Any) -> str:  # noqa: ANN401
        if isinstance(value, str):
            return value
        return str(value)
