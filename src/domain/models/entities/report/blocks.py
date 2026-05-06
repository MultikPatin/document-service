from src.domain.models.entities.base import BaseEntity
from src.domain.models.vo import report


class Single(BaseEntity, report.Single):
    pass


class Table(BaseEntity, report.Table):
    pass
