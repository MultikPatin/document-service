from typing import Protocol

from src.domain.constants import LifeStatusEnum
from src.domain.protocols.pagination import (
    CursorParamsProtocol,
    LimitOffsetParamsProtocol,
    PagesParamsProtocol,
)

type _P = CursorParamsProtocol | LimitOffsetParamsProtocol | PagesParamsProtocol


class LayoutFiltersProtocol[P: _P](Protocol):
    pagination_params: P
    status: LifeStatusEnum | None


class LayoutBlockMessageFiltersProtocol[P: _P](Protocol):
    pagination_params: P


class LayoutBlockSingleFiltersProtocol[P: _P](Protocol):
    pagination_params: P


class LayoutBlockTableFiltersProtocol[P: _P](Protocol):
    pagination_params: P
