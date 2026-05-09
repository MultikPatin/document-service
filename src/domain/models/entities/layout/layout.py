from collections.abc import Sequence

from src.domain.models.entities.base import BaseEntity
from src.domain.models.vo import layout

from .blocks import (
    LayoutBlockMessageEntity,
    LayoutBlockSingleEntity,
    LayoutBlockTableEntity,
)


class LayoutEntity(BaseEntity, layout.Layout):
    singles: Sequence[LayoutBlockMessageEntity] | None
    tables: Sequence[LayoutBlockSingleEntity] | None
    messages: Sequence[LayoutBlockTableEntity] | None
