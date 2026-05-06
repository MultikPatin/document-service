from typing import Any

from libs.mongo.mixins.document_fields import KeyField
from src.adapters.database.mongo.constants import ReportCollections


class ReportBlockTableDocument(KeyField):
    values: list[list[Any]]

    class Settings:
        name = ReportCollections.block_tables()
        max_nesting_depth = 0
