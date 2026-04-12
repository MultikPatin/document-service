from beanie import Document
from pydantic import BaseModel

from .constants import CARD_DOCUMENT_NAME


class LayoutCardTitle(BaseModel):
    path: list[str]


class LayoutBlockCard(Document):
    cells: list[LayoutCardTitle]

    class Settings:
        name = CARD_DOCUMENT_NAME
        max_nesting_depth = 0
