from typing import Any

from libs.mongo.mixins.document_fields import KeyField
from src.infrastructure.mongo.constants import REPORT_BLOCK_SINGLE_COLLECTION


class ReportBlockSingleDocument(KeyField):
    values: dict[str, Any]

    class Settings:
        name = REPORT_BLOCK_SINGLE_COLLECTION
        max_nesting_depth = 0
