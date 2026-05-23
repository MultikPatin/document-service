from pydantic import Field

from src.domain.models.entities import LayoutBlockSingleEntity
from src.infra.mongo.constants import LAYOUT_BLOCK_SINGLE_COLLECTION
from src.infra.mongo.documents.base import DocumentWithKeyLabel
from src.infra.mongo.errors import NoneIDError


class LayoutBlockSingleDocument(DocumentWithKeyLabel):
    ref_count: int = Field(default=0)

    schemas: list[str]
    validations: list[str | None] | None = None
    defaults: list[str | None] | None = None

    def as_entity(self) -> LayoutBlockSingleEntity:
        if self.id is None:
            raise NoneIDError()
        return LayoutBlockSingleEntity(
            id=str(self.id),
            ref_count=self.ref_count,
            key=self.key,
            label=self.label,
            schemas=self.schemas,
            validations=self.validations,
            defaults=self.defaults,
        )

    class Settings:
        name = LAYOUT_BLOCK_SINGLE_COLLECTION
        max_nesting_depth = 0
