from enum import StrEnum, auto
from typing import Final

SEP: Final[str] = "-"

LAYOUT: Final[str] = "layout"
LAYER: Final[str] = "layer"

DEFAULTS: Final[str] = "defaults"
SCHEMAS: Final[str] = "schemas"
VALIDATIONS: Final[str] = "validations"


DEFAULT_DOCUMENT_NAME: Final[str] = f"{LAYOUT}{SEP}{LAYER}{SEP}{DEFAULTS}"
SCHEMA_DOCUMENT_NAME: Final[str] = f"{LAYOUT}{SEP}{LAYER}{SEP}{SCHEMAS}"
VALIDATION_DOCUMENT_NAME: Final[str] = f"{LAYOUT}{SEP}{LAYER}{SEP}{VALIDATIONS}"


class LayoutDataTypeEnum(StrEnum):
    local_dropdown = auto()
    string = auto()
    bool = auto()
    float = auto()
    decimal = auto()
    date = auto()
    time = auto()
    datetime = auto()
    integer = auto()
