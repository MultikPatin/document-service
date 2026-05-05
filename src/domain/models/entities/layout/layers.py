from src.domain.models.mixins import ID
from src.domain.models.vo import layout


class Schema(ID, layout.Schema):
    pass


class Default(ID, layout.Default):
    pass


class Validation(ID, layout.Validation):
    pass
