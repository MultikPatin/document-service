from typing import TYPE_CHECKING

from beanie import Link

from src.infrastructure.mongo.constants import REPORT_COLLECTION
from src.infrastructure.mongo.documents.base import WithTimeStampsDocument

if TYPE_CHECKING:
    from src.infrastructure.mongo.documents import LayoutDocument

    from .blocks import ReportBlockSingleDocument, ReportBlockTableDocument


class ReportDocument(WithTimeStampsDocument):
    singles: list[Link[ReportBlockSingleDocument]] | None = None
    tables: list[Link[ReportBlockTableDocument]] | None = None
    layout: Link[LayoutDocument]

    class Settings:
        name = REPORT_COLLECTION
        max_nesting_depth = 1
        use_state_management = True
