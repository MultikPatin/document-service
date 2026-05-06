from typing import TYPE_CHECKING

from libs.mongo.mixins.repository_methods import AddMixin, GetMixin

from .projections import _LayoutIDProjection

if TYPE_CHECKING:
    from pymongo.asynchronous.client_session import AsyncClientSession

    from src.infrastructure.mongo.enums import KeyEnum


class ReportRepository(GetMixin, AddMixin):
    async def get_full_links[R](
        self,
        document_id: str,
        *,
        session: AsyncClientSession,
        return_as: type[R],
    ) -> R | None:
        document = await self._document.find_one(
            {KeyEnum.id: self.as_id(document_id)},
            session=session,
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

    async def get_layout_id(
        self, document_id: str, *, session: AsyncClientSession
    ) -> str | None:
        document = await self._document.find_one(
            {KeyEnum.id: self.as_id(document_id)},
            session=session,
            projection_model=_LayoutIDProjection,
        )
        if document is None:
            return None
        return document.layout
