from pydantic import Field
from pymongo import HASHED, IndexModel

from libs.mongo.mixins.document_fields import HashField, RefCountField
from src.infrastructure.mongo.constants import LAYOUT_LAYER_DEFAULT_COLLECTION


class LayoutLayerDefaultDocument(RefCountField, HashField):
    value: str | None = Field(default=None)

    class Settings:
        name = LAYOUT_LAYER_DEFAULT_COLLECTION
        max_nesting_depth = 0
        indexes = [  # noqa: RUF012
            IndexModel(
                [("hash", HASHED)],
                name="hash_idx_DESCENDING",
                unique=True,
            )
        ]
