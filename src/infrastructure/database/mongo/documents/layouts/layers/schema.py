from pydantic import Field

from src.infrastructure.database.mongo.documents.constants import (
    LayoutCollections,
    LayoutDataTypeEnum,
)

from .base import BaseDocument, hash_index_class


class LayoutLayerSchemaDocument(BaseDocument):
    key: str = Field(min_length=1, max_length=64)
    label: str = Field(min_length=1, max_length=255)
    required: bool = Field(default=False)
    type: LayoutDataTypeEnum
    # default: str | None = Field(default=None)

    class Settings:
        name = LayoutCollections.layer_schemas()
        max_nesting_depth = 0
        indexes = [hash_index_class]  # noqa: RUF012
