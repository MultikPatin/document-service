from libs.mongo.mixins.document_fields import KeyField
from pydantic import Field

from src.adapters.database.mongo.constants import (
    LayoutCollections,
)


class LayoutBlockSingleDocument(KeyField):
    schemas: list[str]
    validations: list[str | None] | None = Field(default=None)
    defaults: list[str | None] | None = Field(default=None)

    class Settings:
        name = LayoutCollections.block_singles()
        max_nesting_depth = 0
