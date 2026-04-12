from beanie import Document
from pydantic import Field

from .constants import DEFAULT_DOCUMENT_NAME

# from pymongo import DESCENDING, IndexModel


class LayoutLayerDefaultDocument(Document):
    value: str | None = Field(default=None)

    hash: str = Field(min_length=8, max_length=255)
    ref_count: int = Field(default=0)

    class Settings:
        name = DEFAULT_DOCUMENT_NAME
        max_nesting_depth = 0
        # indexes = [
        #     IndexModel(
        #         [("hash", DESCENDING)],
        #         name="hash_idx_DESCENDING",
        #         unique=True,
        #     )
        # ]
