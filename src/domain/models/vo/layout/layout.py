from datetime import datetime

from pydantic import BaseModel

from src.domain.annotations import LayoutSkeletonType
from src.domain.enums import LifeStatusEnum
from src.domain.utils import vo_model_config


class Layout(BaseModel):
    model_config = vo_model_config()

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
