from typing import Any

from src.infrastructure.database.mongo.documents.constants import (
    ReportCollections,
)

from .base import BaseDocument


class ReportBlockTableDocument(BaseDocument):
    values: list[list[Any]]

    class Settings:
        name = ReportCollections.block_tables()
        max_nesting_depth = 0
