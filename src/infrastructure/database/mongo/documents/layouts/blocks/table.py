from pydantic import Field

from src.infrastructure.database.mongo.documents.constants import (
    LayoutCollections,
)

from .base import BaseDocument


class LayoutBlockTableDocument(BaseDocument):
    schemas: list[list[str]]
    validations: list[str | None] | None = Field(default=None)
    defaults: list[list[str | None] | None] | None = Field(default=None)

    class Settings:
        name = LayoutCollections.block_tables()
        max_nesting_depth = 0
