from datetime import datetime

from beanie import Document
from pydantic import Field

from libs.core.time import time_now


class KeyField(Document):
    key: str = Field(min_length=1, max_length=64)


class RefCountField(Document):
    ref_count: int = Field(default=0)


class HashField(Document):
    hash: str = Field(min_length=8, max_length=255)


class CreatedAtField(Document):
    created_at: datetime = Field(default_factory=time_now)


class UpdatedAtField(Document):
    updated_at: datetime = Field(default_factory=time_now)
