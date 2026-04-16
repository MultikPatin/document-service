from collections.abc import Iterable, MutableMapping, Sequence
from typing import TYPE_CHECKING, Any

from beanie import BackLink, Link

if TYPE_CHECKING:
    from beanie import Document
    from pydantic import BaseModel


def link_replacer(obj: MutableMapping[str, Any] | Sequence[Any]) -> None:
    if isinstance(obj, dict):
        to_delete = []
        for k in obj:
            if isinstance(obj[k], Link):  # ty:ignore[invalid-argument-type]
                obj[k] = str(obj[k].ref.id)  # ty:ignore[invalid-assignment, invalid-argument-type]
            elif isinstance(obj[k], BackLink):  # ty:ignore[invalid-argument-type]
                to_delete.append(k)
            else:
                link_replacer(obj[k])  # ty:ignore[invalid-argument-type]
        for k in to_delete:
            del obj[k]
    elif isinstance(obj, list):
        for item in obj:
            link_replacer(item)


def to_dto[DocType: Document, DTO: BaseModel](
    document: DocType, dto: type[DTO], *, replace_links: bool = False
) -> DTO:
    dump = document.model_dump()
    if replace_links:
        link_replacer(dump)
    return dto.model_validate(dump)


def to_dtos[DocType: Document, DTO: BaseModel](
    documents: Iterable[DocType], dto: type[DTO], *, replace_links: bool = False
) -> list[DTO]:
    return [to_dto(d, dto, replace_links=replace_links) for d in documents]
