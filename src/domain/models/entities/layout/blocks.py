from src.domain.annotations import (
    LayoutSingleDefaultLayerType,
    LayoutSingleSchemeLayerType,
    LayoutSingleValidationLayerType,
    LayoutTableDefaultLayerType,
    LayoutTableSchemeLayerType,
    LayoutTableValidationLayerType,
)
from src.domain.models.entities.base import BaseEntity
from src.domain.models.vo import layout


class LayoutBlockMessageEntity(BaseEntity, layout.Message):
    pass


class LayoutBlockSingleEntity(BaseEntity, layout.Single):
    schemas: LayoutSingleSchemeLayerType
    defaults: LayoutSingleDefaultLayerType
    validations: LayoutSingleValidationLayerType


class LayoutBlockTableEntity(BaseEntity, layout.Table):
    schemas: LayoutTableSchemeLayerType
    defaults: LayoutTableDefaultLayerType
    validations: LayoutTableValidationLayerType
