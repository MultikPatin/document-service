from src.domain.entities.mixins import ID
from src.domain.models.vo import report


class Single(ID, report.Single):
    pass


class Table(ID, report.Table):
    pass
