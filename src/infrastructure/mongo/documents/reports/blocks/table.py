from typing import Any

from src.infrastructure.mongo.constants import REPORT_BLOCK_TABLE_COLLECTION
from src.infrastructure.mongo.documents.mixins import Key


class ReportBlockTableDocument(Key):
    values: list[list[Any]]

    class Settings:
        name = REPORT_BLOCK_TABLE_COLLECTION
        max_nesting_depth = 0
