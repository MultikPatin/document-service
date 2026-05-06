from datetime import datetime

from pydantic import BaseModel, ConfigDict

from src.domain.annotations import LayoutSkeletonType
from src.domain.constants import LifeStatusEnum


class Layout(BaseModel):
    model_config = ConfigDict(frozen=True)

    ref_count: int

    key: str
    label: str
    status: LifeStatusEnum

    major_version: int
    minor_version: int

    skeleton: LayoutSkeletonType

    created_at: datetime
    updated_at: datetime | None
    deleted_at: datetime | None
