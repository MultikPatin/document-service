from beanie import Document
from pydantic import Field
from pymongo import HASHED, IndexModel

from src.domain.models.entities import LayoutLayerValidationEntity
from src.infra.mongo.constants import (
    INDEX_HASH_HASHED,
    LAYOUT_LAYER_VALIDATION_COLLECTION,
)
from src.infra.mongo.errors import NoneIDError


class LayoutLayerValidationDocument(Document):
    ref_count: int = Field(default=0)
    hash: str = Field(min_length=8, max_length=255)

    gt: int | None = Field(default=None)
    ge: int | None = Field(default=None)
    lt: int | None = Field(default=None)
    le: int | None = Field(default=None)
    max_digits: int | None = Field(default=None)
    decimal_places: int | None = Field(default=None)
    min_length: int | None = Field(default=None)
    max_length: int | None = Field(default=None)

    def as_entity(self) -> LayoutLayerValidationEntity:
        if self.id is None:
            raise NoneIDError()
        return LayoutLayerValidationEntity(
            id=str(self.id),
            ref_count=self.ref_count,
            hash=self.hash,
            gt=self.gt,
            ge=self.ge,
            lt=self.lt,
            le=self.le,
            max_digits=self.max_digits,
            decimal_places=self.decimal_places,
            min_length=self.min_length,
            max_length=self.max_length,
        )

    class Settings:
        name = LAYOUT_LAYER_VALIDATION_COLLECTION
        max_nesting_depth = 0
        indexes = [  # noqa: RUF012
            IndexModel(
                [("hash", HASHED)],
                name=INDEX_HASH_HASHED,
                unique=True,
            )
        ]
