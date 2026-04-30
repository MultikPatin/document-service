from libs.core.dtos import (
    CreatedAtDTO,
    DescriptionDTO,
    KeyDTO,
    LabelDTO,
    UpdatedAtDTO,
)
from libs.mongo.projections import MongoIDProjection


class _PaginatedLayoutProjection(
    MongoIDProjection,
    KeyDTO,
    LabelDTO,
    UpdatedAtDTO,
    CreatedAtDTO,
    DescriptionDTO,
):
    pass
