from datetime import datetime

from pydantic import BaseModel, ConfigDict


class Report(BaseModel):
    model_config = ConfigDict(frozen=True)

    created_at: datetime
    updated_at: datetime | None
    deleted_at: datetime | None
