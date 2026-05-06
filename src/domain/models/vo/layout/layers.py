from pydantic import BaseModel

from src.domain.enums import DataTypesEnum
from src.domain.utils import vo_model_config


class _Base(BaseModel):
    model_config = vo_model_config()

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
