from pydantic import Field
from pymongo import HASHED, IndexModel

from src.domain.enums import DataTypesEnum
from src.infrastructure.mongo.constants import LAYOUT_LAYER_SCHEMA_COLLECTION
from src.infrastructure.mongo.documents.base import WithKeyLabelDocument


class LayoutLayerSchemaDocument(WithKeyLabelDocument):
    ref_count: int = Field(default=0)
    hash: str = Field(min_length=8, max_length=255)

    required: bool = False
    type: DataTypesEnum

    class Settings:
        name = LAYOUT_LAYER_SCHEMA_COLLECTION
        max_nesting_depth = 0
        indexes = [  # noqa: RUF012
            IndexModel(
                [("hash", HASHED)],
                name="hash_idx_DESCENDING",
                unique=True,
            )
        ]
