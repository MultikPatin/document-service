from collections.abc import Iterable, Set
from enum import StrEnum, auto
from typing import Self


class LayoutBlocksEnum(StrEnum):
    singles = auto()
    tables = auto()
    messages = auto()

    @classmethod
    def fields(cls, exclude: Iterable[Self] | None = None) -> Set[Self]:
        exs = set(exclude) if exclude else set()
        return {m for m in cls if m not in exs}


class LayoutLayersEnum(StrEnum):
    schemas = auto()
    validations = auto()
    styles = auto()
    defaults = auto()

    @classmethod
    def fields(cls, exclude: Iterable[Self] | None = None) -> Set[Self]:
        exs = set(exclude) if exclude else set()
        return {m for m in cls if m not in exs}
