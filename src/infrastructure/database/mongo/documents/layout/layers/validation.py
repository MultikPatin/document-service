from beanie import Document
from pydantic import Field

from .constants import VALIDATION_DOCUMENT_NAME

# from pymongo import DESCENDING, IndexModel


class LayoutLayerValidationDocument(Document):
    gt: int | None = Field(default=None)
    ge: int | None = Field(default=None)
    lt: int | None = Field(default=None)
    le: int | None = Field(default=None)
    max_digits: int | None = Field(default=None)
    decimal_places: int | None = Field(default=None)
    min_length: int | None = Field(default=None)
    max_length: int | None = Field(default=None)

    hash: str = Field(min_length=8, max_length=255)
    ref_count: int = Field(default=0)

    class Settings:
        name = VALIDATION_DOCUMENT_NAME
        max_nesting_depth = 0
        # indexes = [
        #     IndexModel(
        #         [("hash", DESCENDING)],
        #         name="hash_idx_DESCENDING",
        #         unique=True,
        #     )
        # ]
