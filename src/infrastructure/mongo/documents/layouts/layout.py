from typing import TYPE_CHECKING, Any

from beanie import Link
from pydantic import Field
from pymongo import DESCENDING, IndexModel

from src.domain.enums import LifeStatusEnum
from src.infrastructure.mongo.constants import (
    INDEX_KEY_VERSION_DESCENDING,
    LAYOUT_COLLECTION,
)
from src.infrastructure.mongo.documents.base import (
    DocumentWithKeyLabel,
    DocumentWithVersion,
    WithSoftDeleteDocument,
)

if TYPE_CHECKING:
    from .blocks import (
        LayoutBlockMessageDocument,
        LayoutBlockSingleDocument,
        LayoutBlockTableDocument,
    )


class LayoutDocument(
    DocumentWithKeyLabel, DocumentWithVersion, WithSoftDeleteDocument
):
    ref_count: int = Field(default=0)

    status: LifeStatusEnum = Field(default=LifeStatusEnum.created)
    skeleton: list[dict[str, Any]]

    singles: list[Link[LayoutBlockSingleDocument]] | None = None
    tables: list[Link[LayoutBlockTableDocument]] | None = None
    messages: list[Link[LayoutBlockMessageDocument]] | None = None

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
