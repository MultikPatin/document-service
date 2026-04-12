from typing import TYPE_CHECKING

from beanie import Document, Link
from pydantic import Field

from .constants import INPUT_DOCUMENT_NAME

if TYPE_CHECKING:
    from .single import ReportBlockSingle
    from .table import ReportBlockTable


class Report(Document):
    singles: list[Link[ReportBlockSingle]] | None = Field(default=None)
    tables: list[Link[ReportBlockTable]] | None = Field(default=None)
    # layout: Link["LayoutDocument"]

    class Settings:
        name = INPUT_DOCUMENT_NAME
        max_nesting_depth = 1
        use_state_management = True
