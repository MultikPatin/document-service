from pydantic import Field
from pymongo import HASHED, IndexModel

from src.infrastructure.mongo.constants import (
    LAYOUT_LAYER_VALIDATION_COLLECTION,
)
from src.infrastructure.mongo.documents.mixins import Hash, RefCount


class LayoutLayerValidationDocument(RefCount, Hash):
    gt: int | None = Field(default=None)
    ge: int | None = Field(default=None)
    lt: int | None = Field(default=None)
    le: int | None = Field(default=None)
    max_digits: int | None = Field(default=None)
    decimal_places: int | None = Field(default=None)
    min_length: int | None = Field(default=None)
    max_length: int | None = Field(default=None)

    class Settings:
        name = LAYOUT_LAYER_VALIDATION_COLLECTION
        max_nesting_depth = 0
        indexes = [  # noqa: RUF012
            IndexModel(
                [("hash", HASHED)],
                name="hash_idx_DESCENDING",
                unique=True,
            )
        ]
