from collections.abc import Iterable, MutableMapping, Sequence
from typing import TYPE_CHECKING, Any

from beanie import BackLink, Link

if TYPE_CHECKING:
    from beanie import Document


def link_replacer(dump: MutableMapping[str, Any] | Sequence[Any]) -> None:
    if isinstance(dump, dict):
        to_delete = []
        for k in dump:
            if isinstance(dump[k], Link):  # ty:ignore[invalid-argument-type]
                dump[k] = str(dump[k].ref.id)  # ty:ignore[invalid-assignment, invalid-argument-type]
            elif isinstance(dump[k], BackLink):  # ty:ignore[invalid-argument-type]
                to_delete.append(k)
            else:
                link_replacer(dump[k])  # ty:ignore[invalid-argument-type]
        for k in to_delete:
            del dump[k]
    elif isinstance(dump, list):
        for i in dump:
            link_replacer(i)


def to_dto[DocType: Document, ReturnSchema](
    document: DocType,
    return_as: type[ReturnSchema],
    *,
    replace_links: bool = False,
) -> ReturnSchema:
    dump = document.model_dump()
    if replace_links:
        link_replacer(dump)
    return return_as(**dump)


def to_dtos[DocType: Document, ReturnSchema](
    documents: Iterable[DocType],
    return_as: type[ReturnSchema],
    *,
    replace_links: bool = False,
) -> list[ReturnSchema]:
    return [
        to_dto(d, return_as, replace_links=replace_links) for d in documents
    ]
