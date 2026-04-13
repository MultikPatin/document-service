from pydantic import Field

from src.infrastructure.database.mongo.documents.constants import (
    LayoutCollections,
)

from .base import BaseDocument


class LayoutBlockSingleDocument(BaseDocument):
    schemas: list[str]
    validations: list[str | None] | None = Field(default=None)
    defaults: list[str | None] | None = Field(default=None)

    class Settings:
        name = LayoutCollections.block_singles()
        max_nesting_depth = 0
