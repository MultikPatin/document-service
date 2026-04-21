from typing import Any

from pydantic import BaseModel, Field, NegativeInt, field_validator

from libs.core.utils import get_md5hash


class IdDTO(BaseModel):
    id: str = Field(min_length=1)

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
    ref_count: NegativeInt = Field(default=0)

    def can_be_deleted(self) -> bool:
        return self.ref_count == 0


class HashDTO(RefCountDTO):
    hash: str = Field(default="", min_length=8, max_length=255)

    def refresh_hash(self) -> None:
        exclude = {"hash", "id", "ref_count"}
        self.hash = get_md5hash(self.model_dump(exclude=exclude))

    def get_hash(self) -> str:
        self.refresh_hash()
        return self.hash


class RequiredDTO(BaseModel):
    required: bool = Field(default=False)
