from libs.core.dtos import (
    CreatedAtDTO,
    DescriptionDTO,
    KeyDTO,
    LabelDTO,
    UpdatedAtDTO,
)
from libs.mongo.projections import MongoIDProjection


class LayoutShortProjection(
    MongoIDProjection,
    KeyDTO,
    LabelDTO,
    CreatedAtDTO,
    UpdatedAtDTO,
    DescriptionDTO,
):
    pass
