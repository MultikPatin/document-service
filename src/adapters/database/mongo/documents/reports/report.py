from typing import TYPE_CHECKING

from beanie import Link
from pydantic import Field

from libs.mongo.mixins.document_fields import (
    CreatedAtField,
    UpdatedAtField,
)
from src.adapters.database.mongo.constants import ReportCollections

if TYPE_CHECKING:
    from src.adapters.database.mongo.documents import LayoutDocument

    from .blocks import ReportBlockSingleDocument, ReportBlockTableDocument


class ReportDocument(CreatedAtField, UpdatedAtField):
    singles: list[Link[ReportBlockSingleDocument]] | None = Field(default=None)
    tables: list[Link[ReportBlockTableDocument]] | None = Field(default=None)
    layout: Link[LayoutDocument]

    class Settings:
        name = ReportCollections.reports()
        max_nesting_depth = 1
        use_state_management = True
