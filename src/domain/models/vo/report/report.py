from datetime import datetime

from pydantic import BaseModel

from src.domain.utils import vo_model_config


class Report(BaseModel):
    model_config = vo_model_config()

    created_at: datetime
    updated_at: datetime | None
    deleted_at: datetime | None
