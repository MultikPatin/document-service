from pydantic import BaseModel, Field

from src.core.dtos import IdDTO, KeyDTO


class _LayoutSingleBase(BaseModel):
    schemas: list[str]
    validations: list[str | None] | None = Field(default=None)
    defaults: list[str | None] | None = Field(default=None)


class LayoutSingleUpdateDTO(_LayoutSingleBase):
    pass


class LayoutSingleBase(KeyDTO, _LayoutSingleBase):
    pass


class LayoutSingleDB(IdDTO, LayoutSingleBase):
    pass


class LayoutSingleCreateDTO(LayoutSingleBase):
    pass
