from libs.mongo.mixins.repository_methods import (
    AddMixin,
    GetMixin,
    PaginationCursorMixin,
    PaginationLimitOffsetMixin,
    PaginationPagesMixin,
)
from pydantic import BaseModel


class ModelWithHash(BaseModel):
    hash: str | None = None


class _Repository(
    GetMixin,
    AddMixin,
    PaginationCursorMixin,
    PaginationLimitOffsetMixin,
    PaginationPagesMixin,
):
    pass
