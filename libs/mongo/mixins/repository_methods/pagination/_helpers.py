from collections.abc import Iterable
from typing import TYPE_CHECKING

from libs.mongo.converters import to_dtos

if TYPE_CHECKING:
    from pydantic import BaseModel


def convert_items[D: BaseModel, R](
    documents: Iterable[D], return_as: type[R], is_projected: bool
) -> list[R]:
    return (
        [return_as(**d.model_dump()) for d in documents]
        if is_projected
        else to_dtos(documents, return_as, replace_links=True)
    )
