from pydantic import Field

from src.infra.mongo.constants import LAYOUT_BLOCK_SINGLE_COLLECTION
from src.infra.mongo.documents.base import DocumentWithKeyLabel


class LayoutBlockSingleDocument(DocumentWithKeyLabel):
    ref_count: int = Field(default=0)

    schemas: list[str]
    validations: list[str | None] | None = None
    defaults: list[str | None] | None = None

    class Settings:
        name = LAYOUT_BLOCK_SINGLE_COLLECTION
        max_nesting_depth = 0
