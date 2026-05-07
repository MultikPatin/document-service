from typing import Any

from pydantic import BaseModel, ConfigDict, field_validator


class BaseEntity(BaseModel):
    model_config = ConfigDict(frozen=True)

    id: str

    @field_validator("id", mode="before")
    @classmethod
    def convert_id(cls, value: Any) -> str:  # noqa: ANN401
        if isinstance(value, str):
            return value
        return str(value)
