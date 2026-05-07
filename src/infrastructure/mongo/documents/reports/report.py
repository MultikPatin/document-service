from typing import TYPE_CHECKING

from beanie import Link
from pydantic import Field

from src.infrastructure.mongo.constants import REPORT_COLLECTION
from src.infrastructure.mongo.documents.mixins import (
    CreatedAt,
    UpdatedAt,
)

if TYPE_CHECKING:
    from src.infrastructure.mongo.documents import LayoutDocument

    from .blocks import ReportBlockSingleDocument, ReportBlockTableDocument


class ReportDocument(CreatedAt, UpdatedAt):
    singles: list[Link[ReportBlockSingleDocument]] | None = Field(default=None)
    tables: list[Link[ReportBlockTableDocument]] | None = Field(default=None)
    layout: Link[LayoutDocument]

    class Settings:
        name = REPORT_COLLECTION
        max_nesting_depth = 1
        use_state_management = True
