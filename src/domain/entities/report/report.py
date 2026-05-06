from collections.abc import Sequence

from src.domain.entities.layout import Layout
from src.domain.entities.mixins import ID
from src.domain.models.vo import report

from .blocks import Single, Table


class Report(ID, report.Report):
    singles: Sequence[Single] | None
    tables: Sequence[Table] | None
    layout: Layout
