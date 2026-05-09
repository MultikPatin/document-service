from datetime import datetime
from typing import TYPE_CHECKING, Any

from beanie import Document, DocumentWithSoftDelete
from pydantic import Field, NonNegativeInt

from src.domain.utils import time_now
from src.infrastructure.mongo.enums import KeyEnum

if TYPE_CHECKING:
    from beanie import BulkWriter, DeleteRules
    from beanie.odm.actions import ActionDirections
    from pymongo.asynchronous.client_session import AsyncClientSession
    from pymongo.results import DeleteResult


class DocumentWithKey(Document):
    # TODO: Автоматическая генерация если не передан
    key: str = Field(min_length=1, max_length=64)


class DocumentWithKeyLabel(DocumentWithKey):
    label: str = Field(min_length=1, max_length=255)


class DocumentWithVersion(Document):
    major_version: NonNegativeInt = 0
    minor_version: NonNegativeInt = 0

    def version(self) -> str:
        return f"{self.major_version}.{self.minor_version}"

    def increment_major_version(self) -> None:
        self.major_version += 1

    def increment_minor_version(self) -> None:
        self.minor_version += 1


class WithTimeStampsDocument(DocumentWithSoftDelete):
    created_at: datetime
    updated_at: datetime | None

    def set_updated_at(self) -> None:
        self.updated_at = time_now()


class DocumentWithRefs(Document):
    refs: NonNegativeInt = 0

    def increment_refs(self) -> None:
        self.refs += 1

    def decrement_refs(self) -> None:
        if self.refs > 0:
            self.refs -= 1

    def is_referenced_by(self) -> bool:
        return self.refs > 0

    async def delete(
        self,
        session: AsyncClientSession | None = None,
        bulk_writer: BulkWriter | None = None,
        link_rule: DeleteRules = DeleteRules.DO_NOTHING,
        skip_actions: list[ActionDirections | str] | None = None,
        **pymongo_kwargs: Any,  # noqa: ANN401
    ) -> DeleteResult | None:
        document = await self.find_one({KeyEnum.id: self.id})
        if document is None:
            return None
        if self.is_referenced_by():
            return None
        return await super().delete(
            session=session,
            bulk_writer=bulk_writer,
            link_rule=link_rule,
            skip_actions=skip_actions,
            **pymongo_kwargs,
        )
