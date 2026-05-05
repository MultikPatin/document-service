from src.domain.annotations import (
    LayoutSingleDefaultLayerType,
    LayoutSingleSchemeLayerType,
    LayoutSingleValidationLayerType,
    LayoutTableDefaultLayerType,
    LayoutTableSchemeLayerType,
    LayoutTableValidationLayerType,
)
from src.domain.models.mixins import ID
from src.domain.models.vo import layout


class Message(ID, layout.Message):
    pass


class Single(ID, layout.Single):
    schemas: LayoutSingleSchemeLayerType
    defaults: LayoutSingleDefaultLayerType
    validations: LayoutSingleValidationLayerType


class Table(ID, layout.Table):
    schemas: LayoutTableSchemeLayerType
    defaults: LayoutTableDefaultLayerType
    validations: LayoutTableValidationLayerType
