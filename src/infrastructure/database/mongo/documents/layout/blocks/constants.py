from typing import Final

SEP: Final[str] = "-"

LAYOUT: Final[str] = "layout"
BLOCK: Final[str] = "block"

CARDS: Final[str] = "cards"
MESSAGES: Final[str] = "messages"
SINGLES: Final[str] = "singles"
TABLES: Final[str] = "tables"


CARD_DOCUMENT_NAME: Final[str] = f"{LAYOUT}{SEP}{BLOCK}{SEP}{CARDS}"
MESSAGE_DOCUMENT_NAME: Final[str] = f"{LAYOUT}{SEP}{BLOCK}{SEP}{MESSAGES}"
SINGLE_DOCUMENT_NAME: Final[str] = f"{LAYOUT}{SEP}{BLOCK}{SEP}{SINGLES}"
TABLE_DOCUMENT_NAME: Final[str] = f"{LAYOUT}{SEP}{BLOCK}{SEP}{TABLES}"
