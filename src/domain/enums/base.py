from enum import StrEnum, auto


class DataTypesEnum(StrEnum):
    string = auto()
    bool = auto()
    float = auto()
    decimal = auto()
    date = auto()
    time = auto()
    datetime = auto()
    integer = auto()


class LifeStatusEnum(StrEnum):
    created = auto()
    draft = auto()
    published = auto()
    archived = auto()
    deleted = auto()
