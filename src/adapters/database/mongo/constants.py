from abc import ABC, abstractmethod

# from enum import StrEnum, auto
from typing import Final, final


class _CollectionNames(ABC):
    _SEP: Final[str] = "-"
    _BLOCK: Final[str] = "block"
    _CARDS: Final[str] = "cards"
    _SINGLES: Final[str] = "singles"
    _TABLES: Final[str] = "tables"

    @classmethod
    @abstractmethod
    def _base_prefix(cls) -> str:
        pass

    @classmethod
    def _block_prefix(cls) -> str:
        return f"{cls._base_prefix()}{cls._BLOCK}{cls._SEP}"


@final
class ReportCollections(_CollectionNames):
    _REPORT: Final[str] = "report"

    @classmethod
    def reports(cls) -> str:
        return f"{cls._REPORT}s"

    @classmethod
    def _base_prefix(cls) -> str:
        return f"{cls._REPORT}{cls._SEP}"

    @classmethod
    def block_singles(cls) -> str:
        return f"{cls._block_prefix()}{cls._SINGLES}"

    @classmethod
    def block_tables(cls) -> str:
        return f"{cls._block_prefix()}{cls._TABLES}"


@final
class LayoutCollections(_CollectionNames):
    _LAYOUT: Final[str] = "layout"
    _LAYER: Final[str] = "layer"
    _MESSAGES: Final[str] = "messages"
    _DEFAULTS: Final[str] = "defaults"
    _SCHEMAS: Final[str] = "schemas"
    _VALIDATIONS: Final[str] = "validations"

    @classmethod
    def layouts(cls) -> str:
        return f"{cls._LAYOUT}s"

    @classmethod
    def _base_prefix(cls) -> str:
        return f"{cls._LAYOUT}{cls._SEP}"

    @classmethod
    def _layer_prefix(cls) -> str:
        return f"{cls._base_prefix()}{cls._LAYER}{cls._SEP}"

    @classmethod
    def block_singles(cls) -> str:
        return f"{cls._block_prefix()}{cls._SINGLES}"

    @classmethod
    def block_tables(cls) -> str:
        return f"{cls._block_prefix()}{cls._TABLES}"

    @classmethod
    def block_cards(cls) -> str:
        return f"{cls._block_prefix()}{cls._CARDS}"

    @classmethod
    def block_messages(cls) -> str:
        return f"{cls._block_prefix()}{cls._MESSAGES}"

    @classmethod
    def layer_defaults(cls) -> str:
        return f"{cls._layer_prefix()}{cls._DEFAULTS}"

    @classmethod
    def layer_schemas(cls) -> str:
        return f"{cls._layer_prefix()}{cls._SCHEMAS}"

    @classmethod
    def layer_validations(cls) -> str:
        return f"{cls._layer_prefix()}{cls._VALIDATIONS}"


# class LayoutDataTypeEnum(StrEnum):
#     local_dropdown = auto()
#     string = auto()
#     bool = auto()
#     float = auto()
#     decimal = auto()
#     date = auto()
#     time = auto()
#     datetime = auto()
#     integer = auto()
