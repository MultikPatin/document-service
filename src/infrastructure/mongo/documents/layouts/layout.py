from typing import TYPE_CHECKING, Any

from beanie import Link
from pydantic import Field

from src.domain.enums import LifeStatusEnum
from src.infrastructure.mongo.constants import LAYOUT_COLLECTION
from src.infrastructure.mongo.documents.base import (
    WithKeyLabelDocument,
    WithSoftDeleteDocument,
    WithVersionDocument,
)

# from pymongo import DESCENDING, IndexModel
if TYPE_CHECKING:
    from .blocks import (
        LayoutBlockMessageDocument,
        LayoutBlockSingleDocument,
        LayoutBlockTableDocument,
    )


class LayoutDocument(
    WithKeyLabelDocument, WithVersionDocument, WithSoftDeleteDocument
):
    ref_count: int = Field(default=0)

    status: LifeStatusEnum = Field(default=LifeStatusEnum.created)
    skeleton: list[dict[str, Any]]

    singles: list[Link[LayoutBlockSingleDocument]] | None = None
    tables: list[Link[LayoutBlockTableDocument]] | None = None
    messages: list[Link[LayoutBlockMessageDocument]] | None = None

    def version(self) -> str:
        return f"{self.major_version}.{self.minor_version}"

    class Settings:
        name = LAYOUT_COLLECTION
        max_nesting_depth = 1
        use_state_management = True
        # indexes = [
        #     IndexModel(
        #         [
        #             ("major_version", DESCENDING),
        #             ("minor_version", DESCENDING),
        #             ("key", DESCENDING),
        #         ],
        #         name="key_version_unique_idx_DESCENDING",
        #         unique=True,
        #     ),
        # ]
