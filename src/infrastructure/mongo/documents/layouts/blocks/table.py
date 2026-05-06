from pydantic import Field

from libs.mongo.mixins.document_fields import KeyField
from src.infrastructure.mongo.constants import LAYOUT_BLOCK_TABLE_COLLECTION


class LayoutBlockTableDocument(KeyField):
    schemas: list[list[str]]
    validations: list[str | None] | None = Field(default=None)
    defaults: list[list[str | None] | None] | None = Field(default=None)

    class Settings:
        name = LAYOUT_BLOCK_TABLE_COLLECTION
        max_nesting_depth = 0
