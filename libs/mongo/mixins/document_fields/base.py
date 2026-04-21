from beanie import Document
from pydantic import Field


class KeyField(Document):
    key: str = Field(min_length=1, max_length=64)


class RefCountField(Document):
    ref_count: int = Field(default=0)


class HashField(Document):
    hash: str = Field(min_length=8, max_length=255)
