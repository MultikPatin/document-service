from libs.mongo.mixins.document_fields import KeyField
from pydantic import Field

from src.adapters.database.mongo.constants import (
    LayoutCollections,
)


class LayoutBlockTableDocument(KeyField):
    schemas: list[list[str]]
    validations: list[str | None] | None = Field(default=None)
    defaults: list[list[str | None] | None] | None = Field(default=None)

    class Settings:
        name = LayoutCollections.block_tables()
        max_nesting_depth = 0
