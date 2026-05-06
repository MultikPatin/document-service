from pydantic import Field

from libs.mongo.mixins.document_fields import KeyField
from src.infrastructure.mongo.constants import LAYOUT_BLOCK_MESSAGE_COLLECTION


class LayoutBlockMessageDocument(KeyField):
    text: str = Field(min_length=1, max_length=512)

    class Settings:
        name = LAYOUT_BLOCK_MESSAGE_COLLECTION
        max_nesting_depth = 0
