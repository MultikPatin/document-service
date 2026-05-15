from pydantic import Field

from src.infra.mongo.constants import LAYOUT_BLOCK_MESSAGE_COLLECTION
from src.infra.mongo.documents.base import DocumentWithKeyLabel


class LayoutBlockMessageDocument(DocumentWithKeyLabel):
    ref_count: int = Field(default=0)

    text: str = Field(min_length=1, max_length=512)

    class Settings:
        name = LAYOUT_BLOCK_MESSAGE_COLLECTION
        max_nesting_depth = 0
