from typing import Protocol

from libs.core.enums import LifeStatusEnum
from libs.core.protocols.pagination import (
    CursorParamsProtocol,
    LimitOffsetParamsProtocol,
    PagesParamsProtocol,
)

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
