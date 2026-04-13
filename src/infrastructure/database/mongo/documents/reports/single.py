from typing import Any

from src.infrastructure.database.mongo.documents.constants import (
    ReportCollections,
)

from .base import BaseDocument


class ReportBlockSingleDocument(BaseDocument):
    values: dict[str, Any]

    class Settings:
        name = ReportCollections.block_singles()
        max_nesting_depth = 0
