from collections.abc import Iterable
from typing import TYPE_CHECKING

from libs.mongo.converters import to_dtos

if TYPE_CHECKING:
    from pydantic import BaseModel


def convert_items[D: BaseModel, R, P: BaseModel](
    documents: Iterable[D],
    return_as: type[R],
    projection: type[P] | None = None,
) -> list[R]:
    return (
        [return_as(**d.model_dump()) for d in documents]
        if projection
        else to_dtos(documents, return_as, replace_links=True)
    )
