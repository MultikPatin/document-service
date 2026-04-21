from datetime import datetime

from beanie import Document
from pydantic import Field

from libs.core.time import time_now


class CreatedAtField(Document):
    created_at: datetime = Field(default_factory=time_now)


class UpdatedAtField(Document):
    updated_at: datetime = Field(default_factory=time_now)
