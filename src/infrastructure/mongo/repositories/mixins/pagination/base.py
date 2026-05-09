from collections.abc import Iterable
from typing import TYPE_CHECKING

from src.infrastructure.mongo.repositories.mixins import BaseRepository

if TYPE_CHECKING:
    from pydantic import BaseModel


class BasePaginationMixin(BaseRepository):
    def _convert_items[D: BaseModel, R, P: BaseModel](
        self,
        documents: Iterable[D],
        return_as: type[R],
        projection: type[P] | None = None,
    ) -> list[R]:
        return (
            [return_as(**d.model_dump()) for d in documents]
            if projection
            else self.converter.as_dtos(
                documents, return_as, replace_links=True
            )
        )
