from pydantic import Field

from src.infrastructure.database.mongo.documents.constants import (
    LayoutCollections,
)

from .base import BaseDocument, hash_index_class


class LayoutLayerDefaultDocument(BaseDocument):
    value: str | None = Field(default=None)

    class Settings:
        name = LayoutCollections.layer_defaults()
        max_nesting_depth = 0
        indexes = [hash_index_class]  # noqa: RUF012
