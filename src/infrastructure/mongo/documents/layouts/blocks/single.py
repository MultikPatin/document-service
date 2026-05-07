from pydantic import Field

from src.infrastructure.mongo.constants import LAYOUT_BLOCK_SINGLE_COLLECTION
from src.infrastructure.mongo.documents.mixins import Key


class LayoutBlockSingleDocument(Key):
    schemas: list[str]
    validations: list[str | None] | None = Field(default=None)
    defaults: list[str | None] | None = Field(default=None)

    class Settings:
        name = LAYOUT_BLOCK_SINGLE_COLLECTION
        max_nesting_depth = 0
