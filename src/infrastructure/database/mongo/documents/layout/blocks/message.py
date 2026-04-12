from beanie import Document
from pydantic import Field

from .constants import MESSAGE_DOCUMENT_NAME


class LayoutBlockMessage(Document):
    key: str = Field(min_length=1, max_length=64)
    text: str = Field(min_length=1, max_length=512)

    class Settings:
        name = MESSAGE_DOCUMENT_NAME
        max_nesting_depth = 0
