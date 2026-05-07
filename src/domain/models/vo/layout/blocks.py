from pydantic import BaseModel

from src.domain.utils import vo_model_config


class _Base(BaseModel):
    model_config = vo_model_config()

    key: str


class Message(_Base):
    text: str


class Single(_Base):
    pass


class Table(_Base):
    pass
