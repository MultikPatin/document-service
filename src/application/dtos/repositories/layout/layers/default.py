from pydantic import BaseModel, Field

from src.core.dtos import HashDTO, IdDTO


class _LayoutDefaultBase(BaseModel):
    value: str | None = Field(default=None)


class LayoutDefaultUpdateDTO(HashDTO, _LayoutDefaultBase):
    pass


class LayoutDefaultBase(HashDTO, _LayoutDefaultBase):
    pass


class LayoutDefaultDB(IdDTO, _LayoutDefaultBase):
    pass


class LayoutDefaultCreateDTO(HashDTO, _LayoutDefaultBase):
    pass
