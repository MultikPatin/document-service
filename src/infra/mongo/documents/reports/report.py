from typing import TYPE_CHECKING

from beanie import Link

from src.infra.mongo.constants import REPORT_COLLECTION
from src.infra.mongo.documents.base import WithTimeStampsDocument

if TYPE_CHECKING:
    from src.infra.mongo.documents import LayoutDocument

    from .blocks import ReportBlockSingleDocument, ReportBlockTableDocument


class ReportDocument(WithTimeStampsDocument):
    singles: list[Link[ReportBlockSingleDocument]] | None = None
    tables: list[Link[ReportBlockTableDocument]] | None = None
    layout: Link[LayoutDocument]

    class Settings:
        name = REPORT_COLLECTION
        max_nesting_depth = 1
        use_state_management = True
