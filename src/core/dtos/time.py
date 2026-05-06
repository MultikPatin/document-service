from datetime import datetime

from pydantic import BaseModel, Field

from src.domain.utils import time_now


class CreatedAtDTO(BaseModel):
    created_at: datetime = Field(default_factory=time_now)


class UpdatedAtDTO(BaseModel):
    updated_at: datetime = Field(default_factory=time_now)
