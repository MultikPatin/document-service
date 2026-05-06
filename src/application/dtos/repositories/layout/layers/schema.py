from src.core.dtos import (
    HashDTO,
    IdDTO,
    KeyDTO,
    LabelDTO,
    RequiredDTO,
)
from src.domain.enums import DataTypesEnum


class _LayoutSchemaBase(LabelDTO, RequiredDTO):
    pass


class LayoutSchemaUpdateDTO(HashDTO, _LayoutSchemaBase):
    pass


class LayoutSchemaBase(HashDTO, KeyDTO, _LayoutSchemaBase):
    type: DataTypesEnum


class LayoutSchemaDB(IdDTO, LayoutSchemaBase):
    pass


class LayoutSchemaCreateDTO(HashDTO, KeyDTO, _LayoutSchemaBase):
    type: DataTypesEnum
