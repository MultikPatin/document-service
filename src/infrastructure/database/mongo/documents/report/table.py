from typing import Any

from beanie import Document
from pydantic import Field

from .constants import TABLE_DOCUMENT_NAME


class ReportBlockTableDocument(Document):
    key: str = Field(min_length=1, max_length=64)
    values: list[list[Any]]

    class Settings:
        name = TABLE_DOCUMENT_NAME
        max_nesting_depth = 0
