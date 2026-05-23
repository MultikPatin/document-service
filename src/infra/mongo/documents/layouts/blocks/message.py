from pydantic import Field

from src.domain.models.entities import LayoutBlockMessageEntity
from src.infra.mongo.constants import LAYOUT_BLOCK_MESSAGE_COLLECTION
from src.infra.mongo.documents.base import DocumentWithKeyLabel
from src.infra.mongo.errors import NoneIDError


class LayoutBlockMessageDocument(DocumentWithKeyLabel):
    ref_count: int = Field(default=0)

    text: str = Field(min_length=1, max_length=512)

    def as_entity(self) -> LayoutBlockMessageEntity:
        if self.id is None:
            raise NoneIDError()
        return LayoutBlockMessageEntity(
            id=str(self.id),
            ref_count=self.ref_count,
            key=self.key,
            label=self.label,
            text=self.text,
        )

    class Settings:
        name = LAYOUT_BLOCK_MESSAGE_COLLECTION
        max_nesting_depth = 0
