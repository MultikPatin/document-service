from beanie import Document
from pydantic import Field

from src.infrastructure.mongo.constants import LAYOUT_BLOCK_SINGLE_COLLECTION


class LayoutBlockSingleDocument(Document):
    key: str = Field(min_length=1, max_length=64)

    schemas: list[str]
    validations: list[str | None] | None = Field(default=None)
    defaults: list[str | None] | None = Field(default=None)

    class Settings:
        name = LAYOUT_BLOCK_SINGLE_COLLECTION
        max_nesting_depth = 0
