from datetime import datetime

from beanie import Document
from pydantic import Field

from src.domain.utils import time_now


class CreatedAt(Document):
    created_at: datetime = Field(default_factory=time_now)


class UpdatedAt(Document):
    updated_at: datetime = Field(default_factory=time_now)


class Key(Document):
    key: str = Field(min_length=1, max_length=64)


class RefCount(Document):
    ref_count: int = Field(default=0)


class Hash(Document):
    hash: str = Field(min_length=8, max_length=255)
