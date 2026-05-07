from typing import Any

from src.infrastructure.mongo.constants import REPORT_BLOCK_SINGLE_COLLECTION
from src.infrastructure.mongo.documents.mixins import Key


class ReportBlockSingleDocument(Key):
    values: dict[str, Any]

    class Settings:
        name = REPORT_BLOCK_SINGLE_COLLECTION
        max_nesting_depth = 0
