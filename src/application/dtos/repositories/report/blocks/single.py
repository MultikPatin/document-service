from typing import Any

from pydantic import BaseModel

from src.core.dtos import IdDTO, KeyDTO


class InputSingleUpdateDTO(BaseModel):
    values: dict[str, Any]


class InputSingleBase(InputSingleUpdateDTO, KeyDTO):
    pass


class InputSingleDB(IdDTO, InputSingleBase):
    pass


class InputSingleCreateDTO(InputSingleBase):
    pass
