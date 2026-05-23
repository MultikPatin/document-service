from typing import TYPE_CHECKING, Any

from beanie import Link
from pydantic import Field
from pymongo import DESCENDING, IndexModel

from src.domain.enums import LifeStatusEnum
from src.domain.models.entities import LayoutEntity
from src.infra.mongo.constants import (
    INDEX_KEY_VERSION_DESCENDING,
    LAYOUT_COLLECTION,
)
from src.infra.mongo.documents.base import (
    DocumentWithKeyLabel,
    DocumentWithVersion,
    WithTimeStampsDocument,
)
from src.infra.mongo.errors import NoneIDError

if TYPE_CHECKING:
    from .blocks import (
        LayoutBlockMessageDocument,
        LayoutBlockSingleDocument,
        LayoutBlockTableDocument,
    )


class LayoutDocument(
    DocumentWithKeyLabel, DocumentWithVersion, WithTimeStampsDocument
):
    ref_count: int = Field(default=0)

    status: LifeStatusEnum = Field(default=LifeStatusEnum.created)
    skeleton: list[dict[str, Any]]

    singles: list[Link[LayoutBlockSingleDocument]] | None = None
    tables: list[Link[LayoutBlockTableDocument]] | None = None
    messages: list[Link[LayoutBlockMessageDocument]] | None = None

    def as_entity(self) -> LayoutEntity:
        if self.id is None:
            raise NoneIDError()
        return LayoutEntity(
            id=str(self.id),
            ref_count=self.ref_count,
            key=self.key,
            label=self.label,
            status=self.status,
            major_version=self.major_version,
            minor_version=self.minor_version,
            skeleton=self.skeleton,
            created_at=self.created_at,
            updated_at=self.updated_at,
            deleted_at=self.deleted_at,
            singles=None,
            tables=None,
            messages=None,
        )

    class Settings:
        name = LAYOUT_COLLECTION
        max_nesting_depth = 1
        use_state_management = True
        indexes = [  # noqa: RUF012
            IndexModel(
                [
                    ("major_version", DESCENDING),
                    ("minor_version", DESCENDING),
                    ("key", DESCENDING),
                ],
                name=INDEX_KEY_VERSION_DESCENDING,
                unique=True,
            ),
        ]
