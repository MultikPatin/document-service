from pydantic import BaseModel, Field

from libs.core.dtos import IdDTO, KeyDTO


class _LayoutTableBase(BaseModel):
    schemas: list[list[str]]
    validations: list[str | None] | None = Field(default=None)
    defaults: list[list[str | None] | None] | None = Field(default=None)


class LayoutTableUpdateDTO(_LayoutTableBase):
    pass


class LayoutTableBase(KeyDTO, _LayoutTableBase):
    pass


class LayoutTableDB(IdDTO, LayoutTableBase):
    pass


class LayoutTableCreateDTO(LayoutTableBase):
    pass
