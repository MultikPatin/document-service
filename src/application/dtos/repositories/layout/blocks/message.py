from pydantic import BaseModel, Field

from src.core.dtos import IdDTO, KeyDTO


class _LayoutMessageBase(BaseModel):
    text: str = Field(min_length=1, max_length=512)


class LayoutMessageUpdateDTO(BaseModel):
    text: str | None = Field(default=None, min_length=1, max_length=512)


class LayoutMessageBase(KeyDTO, _LayoutMessageBase):
    pass


class LayoutMessageDB(IdDTO, LayoutMessageBase):
    pass


class LayoutMessageCreateDTO(LayoutMessageBase):
    pass
