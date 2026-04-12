from typing import Final

SEP: Final[str] = "-"

INPUT: Final[str] = "input"
BLOCK: Final[str] = "block"

SINGLES: Final[str] = "singles"
TABLES: Final[str] = "tables"


INPUT_DOCUMENT_NAME: Final[str] = f"{INPUT}s"
SINGLE_DOCUMENT_NAME: Final[str] = f"{INPUT}{SEP}{BLOCK}{SEP}{SINGLES}"
TABLE_DOCUMENT_NAME: Final[str] = f"{INPUT}{SEP}{BLOCK}{SEP}{TABLES}"
