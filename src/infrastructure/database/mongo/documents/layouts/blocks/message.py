from pydantic import Field

from src.infrastructure.database.mongo.documents.constants import (
    LayoutCollections,
)

from .base import BaseDocument


class LayoutBlockMessageDocument(BaseDocument):
    text: str = Field(min_length=1, max_length=512)

    class Settings:
        name = LayoutCollections.block_messages()
        max_nesting_depth = 0
