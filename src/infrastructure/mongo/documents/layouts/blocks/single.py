from pydantic import Field

from src.infrastructure.mongo.constants import LAYOUT_BLOCK_SINGLE_COLLECTION
from src.infrastructure.mongo.documents.base import WithKeyLabelDocument


class LayoutBlockSingleDocument(WithKeyLabelDocument):
    ref_count: int = Field(default=0)

    schemas: list[str]
    validations: list[str | None] | None = None
    defaults: list[str | None] | None = None

    class Settings:
        name = LAYOUT_BLOCK_SINGLE_COLLECTION
        max_nesting_depth = 0
