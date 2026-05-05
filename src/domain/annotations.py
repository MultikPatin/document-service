from collections.abc import Mapping, Sequence
from typing import Any

type LayoutSkeletonType = Sequence[Mapping[str, Any]]

type LayoutSingleSchemeLayerType = Sequence[str]
type LayoutSingleDefaultLayerType = Sequence[str | None] | None
type LayoutSingleValidationLayerType = Sequence[str | None] | None

type LayoutTableSchemeLayerType = Sequence[Sequence[str]]
type LayoutTableDefaultLayerType = Sequence[Sequence[str | None] | None] | None
type LayoutTableValidationLayerType = Sequence[str | None] | None

type ReportSingleValuesType = Mapping[str, Any]
type ReportTableValuesType = Sequence[Sequence[Any]]
