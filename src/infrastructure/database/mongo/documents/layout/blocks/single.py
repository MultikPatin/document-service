from beanie import Document
from pydantic import Field

from .constants import SINGLE_DOCUMENT_NAME


class LayoutBlockSingle(Document):
    key: str = Field(min_length=1, max_length=64)

    schemas: list[str]
    validations: list[str | None] | None = Field(default=None)
    defaults: list[str | None] | None = Field(default=None)

    class Settings:
        name = SINGLE_DOCUMENT_NAME
        max_nesting_depth = 0
