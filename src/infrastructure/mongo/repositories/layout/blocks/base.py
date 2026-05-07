from src.infrastructure.mongo.repositories.mixins import (
    AddMixin,
    GetMixin,
    PaginationCursorMixin,
    PaginationLimitOffsetMixin,
    PaginationPagesMixin,
)


class LayoutBlockRepository(
    GetMixin,
    AddMixin,
    PaginationCursorMixin,
    PaginationLimitOffsetMixin,
    PaginationPagesMixin,
):
    pass
