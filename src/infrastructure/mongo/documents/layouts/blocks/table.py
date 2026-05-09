from pydantic import Field

from src.infrastructure.mongo.constants import LAYOUT_BLOCK_TABLE_COLLECTION
from src.infrastructure.mongo.documents.base import DocumentWithKeyLabel


class LayoutBlockTableDocument(DocumentWithKeyLabel):
    ref_count: int = Field(default=0)

    schemas: list[list[str]]
    validations: list[str | None] | None = None
    defaults: list[list[str | None] | None] | None = None

    class Settings:
        name = LAYOUT_BLOCK_TABLE_COLLECTION
        max_nesting_depth = 0
