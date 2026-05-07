from pydantic import Field

from src.infrastructure.mongo.constants import LAYOUT_BLOCK_TABLE_COLLECTION
from src.infrastructure.mongo.documents.mixins import Key


class LayoutBlockTableDocument(Key):
    schemas: list[list[str]]
    validations: list[str | None] | None = Field(default=None)
    defaults: list[list[str | None] | None] | None = Field(default=None)

    class Settings:
        name = LAYOUT_BLOCK_TABLE_COLLECTION
        max_nesting_depth = 0
