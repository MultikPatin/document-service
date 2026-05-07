from pydantic import Field
from pymongo import HASHED, IndexModel

from src.infrastructure.mongo.constants import LAYOUT_LAYER_DEFAULT_COLLECTION
from src.infrastructure.mongo.documents.mixins import Hash, RefCount


class LayoutLayerDefaultDocument(RefCount, Hash):
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
