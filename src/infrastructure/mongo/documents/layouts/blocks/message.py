from beanie import Document
from pydantic import Field

from src.infrastructure.mongo.constants import LAYOUT_BLOCK_MESSAGE_COLLECTION


class LayoutBlockMessageDocument(Document):
    key: str = Field(min_length=1, max_length=64)
    text: str = Field(min_length=1, max_length=512)

    class Settings:
        name = LAYOUT_BLOCK_MESSAGE_COLLECTION
        max_nesting_depth = 0
