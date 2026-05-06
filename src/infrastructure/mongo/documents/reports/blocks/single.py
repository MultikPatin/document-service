from typing import Any

from libs.mongo.mixins.document_fields import KeyField
from src.adapters.database.mongo.constants import ReportCollections


class ReportBlockSingleDocument(KeyField):
    values: dict[str, Any]

    class Settings:
        name = ReportCollections.block_singles()
        max_nesting_depth = 0
