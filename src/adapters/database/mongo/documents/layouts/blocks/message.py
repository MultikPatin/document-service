from pydantic import Field

from libs.mongo.mixins.document_fields import KeyField
from src.adapters.database.mongo.constants import LayoutCollections


class LayoutBlockMessageDocument(KeyField):
    text: str = Field(min_length=1, max_length=512)

    class Settings:
        name = LayoutCollections.block_messages()
        max_nesting_depth = 0
