from pydantic import BaseModel, Field

from src.core.dtos import (
    CreatedAtDTO,
    IdDTO,
    LifeStatusDTO,
    UpdatedAtDTO,
)

from .blocks import (
    InputSingleDB,
    InputSingleUpdateDTO,
    # InputTableDB,
    # InputTableUpdateDTO,
)


class _Base(LifeStatusDTO, UpdatedAtDTO):
    pass


class InputUpdateDTO(_Base):
    singles: list[InputSingleUpdateDTO] | None = Field(default=None)
    # tables: list[InputTableUpdateDTO] | None = Field(default=None)


class InputBase(_Base, CreatedAtDTO):
    pass


class InputDB(IdDTO, InputBase):
    layout: str


class InputWithBlocks(InputDB):
    singles: list[InputSingleDB] | None = Field(default=None)
    # tables: list[InputTableDB] | None = Field(default=None)


class InputCreateDTO(BaseModel):
    layout: str
    singles: list[str] | None = Field(default=None)
    tables: list[str] | None = Field(default=None)
