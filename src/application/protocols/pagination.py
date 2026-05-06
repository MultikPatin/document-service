from typing import Protocol

from src.core.protocols import (
    CursorParamsProtocol,
    LimitOffsetParamsProtocol,
    PagesParamsProtocol,
)
from src.domain.constants import LifeStatusEnum

type _P = CursorParamsProtocol | LimitOffsetParamsProtocol | PagesParamsProtocol


class LayoutPaginationFiltersProtocol[P: _P](Protocol):
    pagination_params: P
    status: LifeStatusEnum | None


class LayoutBlockMessagePaginationFiltersProtocol[P: _P](Protocol):
    pagination_params: P


class LayoutBlockSinglePaginationFiltersProtocol[P: _P](Protocol):
    pagination_params: P


class LayoutBlockTablePaginationFiltersProtocol[P: _P](Protocol):
    pagination_params: P
