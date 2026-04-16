from libs.mongo.mixins.document_fields import HashField, RefCountField
from pydantic import Field
from pymongo import HASHED, IndexModel

from src.adapters.database.mongo.constants import (
    LayoutCollections,
)


class LayoutLayerDefaultDocument(RefCountField, HashField):
    value: str | None = Field(default=None)

    class Settings:
        name = LayoutCollections.layer_defaults()
        max_nesting_depth = 0
        indexes = [  # noqa: RUF012
            IndexModel(
                [("hash", HASHED)],
                name="hash_idx_DESCENDING",
                unique=True,
            )
        ]
