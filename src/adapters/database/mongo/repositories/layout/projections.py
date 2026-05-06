from src.core.dtos import (
    CreatedAtDTO,
    DescriptionDTO,
    KeyDTO,
    LabelDTO,
    UpdatedAtDTO,
)
from src.infrastructure.mongo.projections import IDProjection


class _PaginatedLayoutProjection(
    IDProjection,
    KeyDTO,
    LabelDTO,
    UpdatedAtDTO,
    CreatedAtDTO,
    DescriptionDTO,
):
    pass
