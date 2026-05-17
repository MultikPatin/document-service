from datetime import datetime

from .base import IDProjection


class PaginatedLayoutProjection(IDProjection):
    label: str

    created_at: datetime
    updated_at: datetime | None
