from beanie import Document
from pydantic import BaseModel

from src.infrastructure.database.mongo.documents.constants import (
    LayoutCollections,
)


class LayoutCardTitle(BaseModel):
    path: list[str]


class LayoutBlockCardDocument(Document):
    cells: list[LayoutCardTitle]

    class Settings:
        name = LayoutCollections.block_cards()
        max_nesting_depth = 0
