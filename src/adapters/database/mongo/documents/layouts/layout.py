from typing import TYPE_CHECKING, Any

from beanie import Link
from pydantic import Field

from libs.mongo.mixins.document_fields import (
    CreatedAtField,
    KeyField,
    RefCountField,
    UpdatedAtField,
)
from src.adapters.database.mongo.constants import LayoutCollections
from src.core.enums import LifeStatusEnum

# from pymongo import DESCENDING, IndexModel
if TYPE_CHECKING:
    from .blocks import (
        LayoutBlockMessageDocument,
        LayoutBlockSingleDocument,
        LayoutBlockTableDocument,
    )


class LayoutDocument(KeyField, RefCountField, CreatedAtField, UpdatedAtField):
    label: str = Field(min_length=1, max_length=255)

    major_version: int = Field(ge=0, default=0)
    minor_version: int = Field(ge=0, default=0)
    status: LifeStatusEnum = Field(default=LifeStatusEnum.created)

    skeleton: list[dict[str, Any]]

    singles: list[Link[LayoutBlockSingleDocument]] | None = Field(default=None)
    tables: list[Link[LayoutBlockTableDocument]] | None = Field(default=None)
    messages: list[Link[LayoutBlockMessageDocument]] | None = Field(
        default=None
    )

    class Settings:
        name = LayoutCollections.layouts()
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
