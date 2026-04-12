from typing import Any

from beanie import Document
from pydantic import Field

from .constants import SINGLE_DOCUMENT_NAME


class ReportBlockSingleDocument(Document):
    key: str = Field(min_length=1, max_length=64)
    values: dict[str, Any]

    class Settings:
        name = SINGLE_DOCUMENT_NAME
        max_nesting_depth = 0
