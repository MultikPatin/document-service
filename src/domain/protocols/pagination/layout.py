from typing import Protocol

from src.domain.enums import LifeStatusEnum
from src.domain.protocols.pagination import (
    CursorParamsProtocol,
    LimitOffsetParamsProtocol,
    PagesParamsProtocol,
)

type _P = CursorParamsProtocol | LimitOffsetParamsProtocol | PagesParamsProtocol


class ParamsProtocol[P: _P](Protocol):
    pagination_params: P


class LayoutFiltersProtocol[P: _P](ParamsProtocol[P], Protocol):
    status: LifeStatusEnum | None


class LayoutBlockMessageFiltersProtocol[P: _P](ParamsProtocol[P], Protocol): ...


class LayoutBlockSingleFiltersProtocol[P: _P](ParamsProtocol[P], Protocol): ...


class LayoutBlockTableFiltersProtocol[P: _P](ParamsProtocol[P], Protocol): ...
