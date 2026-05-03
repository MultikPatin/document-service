from pydantic import BaseModel, Field

from src.core.enums import LifeStatusEnum


class LifeStatusDTO(BaseModel):
    status: LifeStatusEnum = Field(default=LifeStatusEnum.created)
