from libs.mongo.mixins.repository_methods import (
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
