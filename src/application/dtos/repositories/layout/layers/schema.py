from libs.core.dtos import (
    HashDTO,
    IdDTO,
    KeyDTO,
    LabelDTO,
    RequiredDTO,
)
from src.application.enums import LayoutDataTypeEnum


class _LayoutSchemaBase(LabelDTO, RequiredDTO):
    pass


class LayoutSchemaUpdateDTO(HashDTO, _LayoutSchemaBase):
    pass


class LayoutSchemaBase(HashDTO, KeyDTO, _LayoutSchemaBase):
    type: LayoutDataTypeEnum


class LayoutSchemaDB(IdDTO, LayoutSchemaBase):
    pass


class LayoutSchemaCreateDTO(HashDTO, KeyDTO, _LayoutSchemaBase):
    type: LayoutDataTypeEnum
