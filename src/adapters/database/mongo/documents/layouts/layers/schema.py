from pydantic import Field
from pymongo import HASHED, IndexModel

from libs.mongo.mixins.document_fields import HashField, RefCountField
from src.adapters.database.mongo.constants import LayoutCollections
from src.domain.enums import DataTypesEnum


class LayoutLayerSchemaDocument(RefCountField, HashField):
    key: str = Field(min_length=1, max_length=64)
    label: str = Field(min_length=1, max_length=255)
    required: bool = Field(default=False)
    type: DataTypesEnum

    class Settings:
        name = LayoutCollections.layer_schemas()
        max_nesting_depth = 0
        indexes = [  # noqa: RUF012
            IndexModel(
                [("hash", HASHED)],
                name="hash_idx_DESCENDING",
                unique=True,
            )
        ]
