from collections.abc import Sequence

from src.domain.models.entities.base import BaseEntity
from src.domain.models.vo import layout

from .blocks import Message, Single, Table


class Layout(BaseEntity, layout.Layout):
    singles: Sequence[Message] | None
    tables: Sequence[Single] | None
    messages: Sequence[Table] | None
