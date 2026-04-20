from pydantic import BaseModel, Field


class PagesParamsDTO(BaseModel):
    number: int = Field(default=1, ge=1)
    size: int = Field(default=50, ge=1, le=100)


class LimitOffsetParamsDTO(BaseModel):
    limit: int = Field(default=50, ge=1, le=100)
    offset: int = Field(default=0, ge=0)


class CursorParamsDTO(BaseModel):
    cursor: str | None = Field(default=None)
    size: int = Field(default=50, ge=1, le=100)
