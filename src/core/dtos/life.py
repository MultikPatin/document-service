from pydantic import BaseModel, Field

from src.domain.constants import LifeStatusEnum


class LifeStatusDTO(BaseModel):
    status: LifeStatusEnum = Field(default=LifeStatusEnum.created)
