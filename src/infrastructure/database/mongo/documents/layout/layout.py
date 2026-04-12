from datetime import datetime
from typing import TYPE_CHECKING, Any

from beanie import Document, Link
from pydantic import Field

from .constants import LAYOUT_DOCUMENT_NAME, LifeStatusEnum
from .utils import time_now

# from pymongo import DESCENDING, IndexModel
if TYPE_CHECKING:
    from .blocks import (
        LayoutBlockCardDocument,
        LayoutBlockMessageDocument,
        LayoutBlockSingleDocument,
        LayoutBlockTableDocument,
    )


class LayoutDocument(Document):
    key: str = Field(min_length=1, max_length=64)
    label: str = Field(min_length=1, max_length=255)
    description: str | None = Field(default=None)

    major_version: int = Field(ge=0, default=0)
    minor_version: int = Field(ge=0, default=0)
    status: LifeStatusEnum = Field(default=LifeStatusEnum.created)

    created_at: datetime = Field(default_factory=time_now)
    updated_at: datetime = Field(default_factory=time_now)

    options: dict[str, Any] | None = Field(default=None)
    ref_count: int = Field(default=0)

    skeleton: list[dict[str, Any]]

    card: Link[LayoutBlockCardDocument] | None = Field(default=None)
    singles: list[Link[LayoutBlockSingleDocument]] | None = Field(default=None)
    tables: list[Link[LayoutBlockTableDocument]] | None = Field(default=None)
    messages: list[Link[LayoutBlockMessageDocument]] | None = Field(
        default=None
    )

    class Settings:
        name = LAYOUT_DOCUMENT_NAME
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
