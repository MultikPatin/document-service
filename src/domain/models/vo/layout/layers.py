from pydantic import BaseModel, ConfigDict

from src.domain.constants import DataTypesEnum


class _Base(BaseModel):
    model_config = ConfigDict(frozen=True)

    hash: str
    ref_count: int


class Schema(_Base):
    key: str
    label: str
    type: DataTypesEnum
    required: bool


class Default(_Base):
    value: str | None


class Validation(_Base):
    gt: int | None
    ge: int | None
    lt: int | None
    le: int | None
    max_digits: int | None
    decimal_places: int | None
    min_length: int | None
    max_length: int | None
