from pydantic import Field
from pymongo import HASHED, IndexModel

from src.domain.enums import DataTypesEnum
from src.infrastructure.mongo.constants import LAYOUT_LAYER_SCHEMA_COLLECTION
from src.infrastructure.mongo.documents.mixins import Hash, RefCount


class LayoutLayerSchemaDocument(RefCount, Hash):
    key: str = Field(min_length=1, max_length=64)
    label: str = Field(min_length=1, max_length=255)
    required: bool = Field(default=False)
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
