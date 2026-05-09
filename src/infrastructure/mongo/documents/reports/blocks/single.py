from typing import Any

from src.infrastructure.mongo.constants import REPORT_BLOCK_SINGLE_COLLECTION
from src.infrastructure.mongo.documents.base import WithKeyDocument


class ReportBlockSingleDocument(WithKeyDocument):
    values: dict[str, Any]

    class Settings:
        name = REPORT_BLOCK_SINGLE_COLLECTION
        max_nesting_depth = 0
