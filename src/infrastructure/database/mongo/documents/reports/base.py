from beanie import Document
from pydantic import Field


class BaseDocument(Document):
    key: str = Field(min_length=1, max_length=64)
