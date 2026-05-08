from typing import TYPE_CHECKING

from src.infrastructure.mongo.projections import LayoutIDProjection
from src.infrastructure.mongo.repositories.mixins import AddMixin, GetMixin

if TYPE_CHECKING:
    from src.infrastructure.mongo.enums import KeyEnum


class ReportRepository(GetMixin, AddMixin):
    async def get_full_links[R](
        self, id_: str, *, return_as: type[R]
    ) -> R | None:
        document = await self._document.find_one(
            {KeyEnum.id: self.as_id(id_)},
            session=self._session,
            fetch_links=True,
            nesting_depths_per_field={
                "layout": 0,
                "singles": 1,
                "tables": 1,
            },
        )
        if document is None:
            return None
        return self.as_dto(document, return_as, replace_links=True)

    async def get_layout_id(self, id_: str) -> str | None:
        document = await self._document.find_one(
            {KeyEnum.id: self.as_id(id_)},
            session=self._session,
            projection_model=LayoutIDProjection,
        )
        if document is None:
            return None
        return document.layout
