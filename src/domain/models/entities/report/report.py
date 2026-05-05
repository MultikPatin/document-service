from collections.abc import Sequence

from src.domain.models.entities.layout import Layout
from src.domain.models.mixins import ID
from src.domain.models.vo import report

from .blocks import Single, Table


class Report(ID, report.Report):
    singles: Sequence[Single] | None
    tables: Sequence[Table] | None
    layout: Layout
