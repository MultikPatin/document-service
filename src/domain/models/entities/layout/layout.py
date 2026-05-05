from collections.abc import Sequence

from src.domain.models.mixins import ID

from .blocks import Message, Single, Table


class Layout(ID):
    singles: Sequence[Message] | None
    tables: Sequence[Single] | None
    messages: Sequence[Table] | None
