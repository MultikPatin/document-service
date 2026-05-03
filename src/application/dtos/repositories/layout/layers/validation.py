from pydantic import BaseModel, Field

from src.core.dtos import HashDTO, IdDTO


class _LayoutValidationBase(BaseModel):
    gt: int | None = Field(default=None)
    ge: int | None = Field(default=None)
    lt: int | None = Field(default=None)
    le: int | None = Field(default=None)
    max_digits: int | None = Field(default=None)
    decimal_places: int | None = Field(default=None)
    min_length: int | None = Field(default=None)
    max_length: int | None = Field(default=None)


class LayoutValidationUpdateDTO(HashDTO, _LayoutValidationBase):
    pass


class LayoutValidationBase(HashDTO, _LayoutValidationBase):
    pass


class LayoutValidationDB(IdDTO, LayoutValidationBase):
    pass


class LayoutValidationCreateDTO(HashDTO, _LayoutValidationBase):
    pass
