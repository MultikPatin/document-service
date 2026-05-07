from collections.abc import Iterable
from typing import TYPE_CHECKING

from src.infrastructure.mongo.repositories.mixins import BaseRepository

if TYPE_CHECKING:
    from pydantic import BaseModel


class BasePaginationMixin(BaseRepository):
    def _convert_items[D: BaseModel, R, P: BaseModel](
        self, docs: Iterable[D], dto: type[R], projection: type[P] | None = None
    ) -> list[R]:
        return (
            [dto(**d.model_dump()) for d in docs]
            if projection
            else self.as_dtos(docs, dto, replace_links=True)
        )
