from pydantic import Field

from src.infrastructure.database.mongo.documents.constants import (
    LayoutCollections,
)

from .base import BaseDocument, hash_index_class


class LayoutLayerValidationDocument(BaseDocument):
    gt: int | None = Field(default=None)
    ge: int | None = Field(default=None)
    lt: int | None = Field(default=None)
    le: int | None = Field(default=None)
    max_digits: int | None = Field(default=None)
    decimal_places: int | None = Field(default=None)
    min_length: int | None = Field(default=None)
    max_length: int | None = Field(default=None)

    class Settings:
        name = LayoutCollections.layer_validations()
        max_nesting_depth = 0
        indexes = [hash_index_class]  # noqa: RUF012
