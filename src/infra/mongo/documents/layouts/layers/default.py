from beanie import Document
from pydantic import Field
from pymongo import HASHED, IndexModel

from src.infra.mongo.constants import (
    INDEX_HASH_HASHED,
    LAYOUT_LAYER_DEFAULT_COLLECTION,
)


class LayoutLayerDefaultDocument(Document):
    ref_count: int = Field(default=0)
    hash: str = Field(min_length=8, max_length=255)

    value: str | None = Field(default=None)

    class Settings:
        name = LAYOUT_LAYER_DEFAULT_COLLECTION
        max_nesting_depth = 0
        indexes = [  # noqa: RUF012
            IndexModel(
                [("hash", HASHED)],
                name=INDEX_HASH_HASHED,
                unique=True,
            )
        ]
