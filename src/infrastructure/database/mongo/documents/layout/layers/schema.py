from beanie import Document
from pydantic import Field

from .constants import SCHEMA_DOCUMENT_NAME, LayoutDataTypeEnum

# from pymongo import DESCENDING, IndexModel


class LayoutLayerSchema(Document):
    key: str = Field(min_length=1, max_length=64)
    label: str = Field(min_length=1, max_length=255)
    required: bool = Field(default=False)
    type: LayoutDataTypeEnum
    # default: str | None = Field(default=None)

    hash: str = Field(min_length=8, max_length=255)
    ref_count: int = Field(default=0)

    class Settings:
        name = SCHEMA_DOCUMENT_NAME
        max_nesting_depth = 0
        # indexes = [
        #     IndexModel(
        #         [("hash", DESCENDING)],
        #         name="hash_idx_DESCENDING",
        #         unique=True,
        #     )
        # ]
