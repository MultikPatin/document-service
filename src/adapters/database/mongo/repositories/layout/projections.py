from libs.mongo.projections import MongoIDProjection
from src.core.dtos import (
    CreatedAtDTO,
    DescriptionDTO,
    KeyDTO,
    LabelDTO,
    UpdatedAtDTO,
)


class _PaginatedLayoutProjection(
    MongoIDProjection,
    KeyDTO,
    LabelDTO,
    UpdatedAtDTO,
    CreatedAtDTO,
    DescriptionDTO,
):
    pass
