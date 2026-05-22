from beanie import Document
from pydantic import Field
from pymongo import HASHED, IndexModel

from src.domain.models.entities import LayoutLayerDefaultEntity
from src.infra.mongo.constants import (
    INDEX_HASH_HASHED,
    LAYOUT_LAYER_DEFAULT_COLLECTION,
)
from src.infra.mongo.errors import NoneIDError


class LayoutLayerDefaultDocument(Document):
    ref_count: int = Field(default=0)
    hash: str = Field(min_length=8, max_length=255)

    value: str | None = Field(default=None)

    def as_entity(self) -> LayoutLayerDefaultEntity:
        if self.id is None:
            raise NoneIDError()
        return LayoutLayerDefaultEntity(
            id=str(self.id),
            ref_count=self.ref_count,
            hash=self.hash,
            value=self.value,
        )

    class Settings:
        name = LAYOUT_LAYER_DEFAULT_COLLECTION
        max_nesting_depth = 0
        indexes = [  # noqa: RUF012
            IndexModel(
                [("hash", HASHED)],
                name=INDEX_HASH_HASHED,
                unique=True,
            )
        ]
