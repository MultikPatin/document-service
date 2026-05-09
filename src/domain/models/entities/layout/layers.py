from src.domain.models.entities.base import BaseEntity
from src.domain.models.vo import layout


class LayoutLayerSchemaEntity(BaseEntity, layout.Schema):
    pass


class LayoutLayerDefaultEntity(BaseEntity, layout.Default):
    pass


class LayoutLayerValidationEntity(BaseEntity, layout.Validation):
    pass
