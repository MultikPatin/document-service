from typing import TYPE_CHECKING, Any

from beanie import Link
from bson import DBRef
from libs.mongo.converters import to_dto, to_poid
from libs.mongo.mixins.repository_methods import AddMixin, GetMixin
from pydantic import field_validator

if TYPE_CHECKING:
    from libs.mongo.enums import KeyEnum
    from pydantic import BaseModel
    from pymongo.asynchronous.client_session import AsyncClientSession


# TODO Перенести
class ReportLayoutIDProjection(BaseModel):
    layout: str

    @field_validator("layout", mode="before")
    @classmethod
    def convert_layout(cls, value: Any) -> str:  # noqa: ANN401
        if isinstance(value, DBRef):
            return str(value.id)
        if isinstance(value, Link):
            return str(value.ref.id)
        return str(value)


class ReportRepository(GetMixin, AddMixin):
    async def get_full_links[ReturnSchema: BaseModel](
        self,
        document_id: str,
        *,
        session: AsyncClientSession,
        return_as: type[ReturnSchema],
    ) -> ReturnSchema | None:
        document = await self._document.find_one(
            {KeyEnum.id: to_poid(document_id)},
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
        return to_dto(document, return_as, replace_links=True)

    async def get_layout_id(
        self, document_id: str, *, session: AsyncClientSession
    ) -> str | None:
        document = await self._document.find_one(
            {KeyEnum.id: to_poid(document_id)},
            session=session,
            projection_model=ReportLayoutIDProjection,
        )
        if document is None:
            return None
        return document.layout
