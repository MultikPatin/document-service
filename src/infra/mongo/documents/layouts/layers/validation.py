from beanie import Document
from pydantic import Field
from pymongo import HASHED, IndexModel

from src.infra.mongo.constants import (
    INDEX_HASH_HASHED,
    LAYOUT_LAYER_VALIDATION_COLLECTION,
)


class LayoutLayerValidationDocument(Document):
    ref_count: int = Field(default=0)
    hash: str = Field(min_length=8, max_length=255)

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
                name=INDEX_HASH_HASHED,
                unique=True,
            )
        ]
