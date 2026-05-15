from typing import Any

from src.infra.mongo.constants import REPORT_BLOCK_SINGLE_COLLECTION
from src.infra.mongo.documents.base import DocumentWithKey


class ReportBlockSingleDocument(DocumentWithKey):
    values: dict[str, Any]

    class Settings:
        name = REPORT_BLOCK_SINGLE_COLLECTION
        max_nesting_depth = 0
