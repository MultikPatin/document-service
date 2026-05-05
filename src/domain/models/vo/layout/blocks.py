from pydantic import BaseModel, ConfigDict


class _Base(BaseModel):
    model_config = ConfigDict(frozen=True)

    key: str


class Message(_Base):
    text: str


class Single(_Base):
    pass


class Table(_Base):
    pass
