from pydantic import BaseModel, ConfigDict

from src.domain.annotations import ReportSingleValuesType, ReportTableValuesType


class _Base(BaseModel):
    model_config = ConfigDict(frozen=True)

    key: str


class Single(_Base):
    values: ReportSingleValuesType


class Table(_Base):
    values: ReportTableValuesType
