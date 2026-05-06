from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from src.domain.protocols.pagination import (
        CursorParamsProtocol,
        LayoutBlockMessageFiltersProtocol,
        LayoutBlockSingleFiltersProtocol,
        LayoutBlockTableFiltersProtocol,
        LayoutFiltersProtocol,
        LimitOffsetParamsProtocol,
        PagesParamsProtocol,
    )

type LayoutSkeletonType = Sequence[Mapping[str, Any]]

type LayoutSingleSchemeLayerType = Sequence[str]
type LayoutSingleDefaultLayerType = Sequence[str | None] | None
type LayoutSingleValidationLayerType = Sequence[str | None] | None

type LayoutTableSchemeLayerType = Sequence[Sequence[str]]
type LayoutTableDefaultLayerType = Sequence[Sequence[str | None] | None] | None
type LayoutTableValidationLayerType = Sequence[str | None] | None


type LayoutPageFiltersType = LayoutFiltersProtocol[PagesParamsProtocol]
type LayoutLimitOffsetFiltersType = LayoutFiltersProtocol[
    LimitOffsetParamsProtocol
]
type LayoutCursorFiltersType = LayoutFiltersProtocol[CursorParamsProtocol]


type LayoutMessagePageFiltersType = LayoutBlockMessageFiltersProtocol[
    PagesParamsProtocol
]
type LayoutMessageLimitOffsetFiltersType = LayoutBlockMessageFiltersProtocol[
    LimitOffsetParamsProtocol
]
type LayoutMessageCursorFiltersType = LayoutBlockMessageFiltersProtocol[
    CursorParamsProtocol
]


type LayoutSinglePageFiltersType = LayoutBlockSingleFiltersProtocol[
    PagesParamsProtocol
]
type LayoutSingleLimitOffsetFiltersType = LayoutBlockSingleFiltersProtocol[
    LimitOffsetParamsProtocol
]
type LayoutSingleCursorFiltersType = LayoutBlockSingleFiltersProtocol[
    CursorParamsProtocol
]


type LayoutTablePageFiltersType = LayoutBlockTableFiltersProtocol[
    PagesParamsProtocol
]
type LayoutTableLimitOffsetFiltersType = LayoutBlockTableFiltersProtocol[
    LimitOffsetParamsProtocol
]
type LayoutTableCursorFiltersType = LayoutBlockTableFiltersProtocol[
    CursorParamsProtocol
]
