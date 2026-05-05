from collections.abc import Sequence

from src.domain.models.mixins import ID
from src.domain.models.vo import layout

from .blocks import Message, Single, Table


class Layout(ID, layout.Layout):
    singles: Sequence[Message] | None
    tables: Sequence[Single] | None
    messages: Sequence[Table] | None
