from beanie import Document
from pydantic import Field

from .constants import TABLE_DOCUMENT_NAME


class LayoutBlockTable(Document):
    key: str = Field(min_length=1, max_length=64)

    schemas: list[list[str]]
    validations: list[str | None] | None = Field(default=None)
    defaults: list[list[str | None] | None] | None = Field(default=None)

    class Settings:
        name = TABLE_DOCUMENT_NAME
        max_nesting_depth = 0
