from collections.abc import Mapping, Sequence
from typing import Any

type LayoutSkeletonType = Sequence[Mapping[str, Any]]


type ReportSingleValuesType = Mapping[str, Any]
type ReportTableValuesType = Sequence[Sequence[Any]]
