from src.domain.entities.base import BaseEntity
from src.domain.models.vo import layout


class Schema(BaseEntity, layout.Schema):
    pass


class Default(BaseEntity, layout.Default):
    pass


class Validation(BaseEntity, layout.Validation):
    pass
