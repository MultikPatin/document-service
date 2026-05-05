from datetime import datetime

from pydantic import BaseModel, ConfigDict

from src.domain.annotations import LayoutSkeletonType
from src.domain.constants import LifeStatusEnum


class Layout(BaseModel):
    model_config = ConfigDict(frozen=True)

    ref_count: int

    created_at: datetime
    updated_at: datetime | None
    deleted_at: datetime | None

    key: str
    label: str
    description: str | None

    major_version: int
    minor_version: int

    status: LifeStatusEnum

    skeleton: LayoutSkeletonType
