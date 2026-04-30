from typing import Any

from pydantic import Field

from libs.core.dtos import (
    CreatedAtDTO,
    DescriptionDTO,
    IdDTO,
    KeyDTO,
    LabelDTO,
    LifeStatusDTO,
    MajorVersionDTO,
    MinorVersionDTO,
    RefCountDTO,
    UpdatedAtDTO,
)

from .blocks import (
    LayoutMessageCreateDTO,
    LayoutMessageDB,
    LayoutMessageUpdateDTO,
    LayoutSingleCreateDTO,
    LayoutSingleDB,
    LayoutSingleUpdateDTO,
    LayoutTableCreateDTO,
    LayoutTableDB,
    LayoutTableUpdateDTO,
)


class _LayoutShort(LabelDTO, UpdatedAtDTO, DescriptionDTO):
    pass


class _LayoutBase(_LayoutShort, UpdatedAtDTO, LifeStatusDTO):
    skeleton: list[dict[str, Any]]


# Update


class LayoutUpdateDTO(_LayoutBase):
    singles: list[LayoutSingleUpdateDTO] | None = Field(default=None)
    tables: list[LayoutTableUpdateDTO] | None = Field(default=None)
    messages: list[LayoutMessageUpdateDTO] | None = Field(default=None)


# Base


class LayoutBase(
    _LayoutBase,
    KeyDTO,
    RefCountDTO,
    MajorVersionDTO,
    MinorVersionDTO,
    CreatedAtDTO,
):
    pass


class LayoutShortDTO(IdDTO, KeyDTO, _LayoutShort, CreatedAtDTO):
    pass


class LayoutDB(IdDTO, LayoutBase):
    pass


class LayoutWithBlocks(LayoutDB):
    singles: list[LayoutSingleDB] | None = Field(default=None)
    tables: list[LayoutTableDB] | None = Field(default=None)
    messages: list[LayoutMessageDB] | None = Field(default=None)


class LayoutFullLinks(LayoutWithBlocks):
    pass


# Create


class LayoutCreateDTO(LayoutBase):
    singles: list[LayoutSingleCreateDTO] | None = Field(default=None)
    tables: list[LayoutTableCreateDTO] | None = Field(default=None)
    messages: list[LayoutMessageCreateDTO] | None = Field(default=None)
