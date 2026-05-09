from typing import Any

from beanie import Document
from pydantic import Field

from src.infrastructure.mongo.constants import REPORT_BLOCK_TABLE_COLLECTION


class ReportBlockTableDocument(Document):
    key: str = Field(min_length=1, max_length=64)
    values: list[list[Any]]

    class Settings:
        name = REPORT_BLOCK_TABLE_COLLECTION
        max_nesting_depth = 0
