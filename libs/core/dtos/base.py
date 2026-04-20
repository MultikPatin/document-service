from typing import Any

from pydantic import BaseModel, Field, field_validator


class IdDTO(BaseModel):
    id: str

    @field_validator("id", mode="before")
    @classmethod
    def convert_id(cls, value: Any) -> str:  # noqa: ANN401
        if isinstance(value, str):
            return value
        return str(value)


class KeyDTO(BaseModel):
    key: str = Field(min_length=1, max_length=64)


class LabelDTO(BaseModel):
    label: str = Field(min_length=1, max_length=255)


class TitleDTO(BaseModel):
    title: str = Field(min_length=1, max_length=255)


class DescriptionDTO(BaseModel):
    description: str | None = Field(default=None)


class RefCountDTO(BaseModel):
    ref_count: int = Field(default=0)


class HashDTO(RefCountDTO):
    hash: str = Field(min_length=8, max_length=255)


class RequiredDTO(BaseModel):
    required: bool = Field(default=False)
