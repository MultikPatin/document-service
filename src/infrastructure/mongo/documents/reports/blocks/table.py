from typing import Any

from libs.mongo.mixins.document_fields import KeyField
from src.infrastructure.mongo.constants import REPORT_BLOCK_TABLE_COLLECTION


class ReportBlockTableDocument(KeyField):
    values: list[list[Any]]

    class Settings:
        name = REPORT_BLOCK_TABLE_COLLECTION
        max_nesting_depth = 0
