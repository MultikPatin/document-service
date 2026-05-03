from collections.abc import Iterable, Sequence
from typing import TYPE_CHECKING

from .converters import BaseConverters

if TYPE_CHECKING:
    from beanie import Document, PydanticObjectId
    from pydantic import BaseModel


class BaseRepository:
    def __init__[DocType: Document](
        self,
        document: type[DocType],
        converters: BaseConverters | None = None,
    ) -> None:
        self._document = document
        self._converters = converters if converters else BaseConverters()

    def as_id(self, _id: str, /) -> PydanticObjectId:
        return self._converters.as_id(_id)

    def as_ids(self, ids: Sequence[str], /) -> Sequence[PydanticObjectId]:
        return self._converters.as_ids(ids)

    def as_dto[D: BaseModel, R](
        self, doc: D, dto: type[R], *, replace_links: bool = False
    ) -> R:
        return self._converters.as_dto(doc, dto, replace_links=replace_links)

    def as_dtos[D: BaseModel, R](
        self, docs: Iterable[D], dto: type[R], *, replace_links: bool = False
    ) -> list[R]:
        return self._converters.as_dtos(docs, dto, replace_links=replace_links)
