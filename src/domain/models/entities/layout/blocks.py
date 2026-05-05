from src.domain.models.mixins import ID


class Message(ID):
    pass


class Single(ID):
    schemas: list[str]
    validations: list[str | None] | None
    defaults: list[str | None] | None


class Table(ID):
    schemas: list[list[str]]
    validations: list[str | None] | None
    defaults: list[list[str | None] | None] | None
