from pydantic import BaseModel

from src.domain.annotations import ReportSingleValuesType, ReportTableValuesType
from src.domain.utils import vo_model_config


class _Base(BaseModel):
    model_config = vo_model_config()

    key: str


class Single(_Base):
    values: ReportSingleValuesType


class Table(_Base):
    values: ReportTableValuesType
