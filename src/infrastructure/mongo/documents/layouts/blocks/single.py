from pydantic import Field

from libs.mongo.mixins.document_fields import KeyField
from src.infrastructure.mongo.constants import LAYOUT_BLOCK_SINGLE_COLLECTION


class LayoutBlockSingleDocument(KeyField):
    schemas: list[str]
    validations: list[str | None] | None = Field(default=None)
    defaults: list[str | None] | None = Field(default=None)

    class Settings:
        name = LAYOUT_BLOCK_SINGLE_COLLECTION
        max_nesting_depth = 0
