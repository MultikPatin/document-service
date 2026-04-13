from typing import TYPE_CHECKING

from beanie import Document, Link
from pydantic import Field

from src.infrastructure.database.mongo.documents.constants import (
    ReportCollections,
)

if TYPE_CHECKING:
    from .single import ReportBlockSingleDocument
    from .table import ReportBlockTableDocument


class ReportDocument(Document):
    singles: list[Link[ReportBlockSingleDocument]] | None = Field(default=None)
    tables: list[Link[ReportBlockTableDocument]] | None = Field(default=None)
    # layout: Link["LayoutDocument"]

    class Settings:
        name = ReportCollections.reports()
        max_nesting_depth = 1
        use_state_management = True
