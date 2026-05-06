from datetime import datetime

from beanie import Document
from pydantic import Field

from src.domain.utils import time_now


class CreatedAtField(Document):
    created_at: datetime = Field(default_factory=time_now)


class UpdatedAtField(Document):
    updated_at: datetime = Field(default_factory=time_now)
