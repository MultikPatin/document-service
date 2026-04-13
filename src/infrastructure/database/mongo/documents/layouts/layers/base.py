from beanie import Document
from pydantic import Field
from pymongo import DESCENDING, IndexModel

hash_index_class = IndexModel(
    [("hash", DESCENDING)],
    name="hash_idx_DESCENDING",
    unique=True,
)


class BaseDocument(Document):
    hash: str = Field(min_length=8, max_length=255)
    ref_count: int = Field(default=0)
