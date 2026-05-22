from pydantic import Field
from pymongo import HASHED, IndexModel

from src.domain.enums import DataTypesEnum
from src.domain.models.entities import LayoutLayerSchemaEntity
from src.infra.mongo.constants import (
    INDEX_HASH_HASHED,
    LAYOUT_LAYER_SCHEMA_COLLECTION,
)
from src.infra.mongo.documents.base import DocumentWithKeyLabel
from src.infra.mongo.errors import NoneIDError


class LayoutLayerSchemaDocument(DocumentWithKeyLabel):
    ref_count: int = Field(default=0)
    hash: str = Field(min_length=8, max_length=255)

    required: bool = False
    type: DataTypesEnum

    def as_entity(self) -> LayoutLayerSchemaEntity:
        if self.id is None:
            raise NoneIDError()
        return LayoutLayerSchemaEntity(
            id=str(self.id),
            ref_count=self.ref_count,
            hash=self.hash,
            key=self.key,
            label=self.label,
            required=self.required,
            type=self.type,
        )

    class Settings:
        name = LAYOUT_LAYER_SCHEMA_COLLECTION
        max_nesting_depth = 0
        indexes = [  # noqa: RUF012
            IndexModel(
                [("hash", HASHED)],
                name=INDEX_HASH_HASHED,
                unique=True,
            )
        ]
