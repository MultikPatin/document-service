from typing import Final

_S = "s"
_SEP: Final[str] = "-"

_L: Final[str] = "layout"
_R: Final[str] = "report"

_BLOCK: Final[str] = "block"
_SINGLE: Final[str] = "single"
_TABLE: Final[str] = "table"
_MESSAGE: Final[str] = "message"

_LAYER: Final[str] = "layer"
_DEFAULT: Final[str] = "default"
_SCHEMA: Final[str] = "schema"
_VALID: Final[str] = "validation"

_RBLOCK: Final[str] = _R + _SEP + _BLOCK

_LBLOCK: Final[str] = _L + _SEP + _BLOCK
_LLAYER: Final[str] = _L + _SEP + _LAYER


LAYOUT_COLLECTION: Final[str] = _L + _S

LAYOUT_BLOCK_SINGLE_COLLECTION: Final[str] = _LBLOCK + _SEP + _SINGLE + _S
LAYOUT_BLOCK_TABLE_COLLECTION: Final[str] = _LBLOCK + _SEP + _TABLE + _S
LAYOUT_BLOCK_MESSAGE_COLLECTION: Final[str] = _LBLOCK + _SEP + _MESSAGE + _S

LAYOUT_LAYER_DEFAULT_COLLECTION: Final[str] = _LLAYER + _SEP + _DEFAULT + _S
LAYOUT_LAYER_SCHEMA_COLLECTION: Final[str] = _LLAYER + _SEP + _SCHEMA + _S
LAYOUT_LAYER_VALIDATION_COLLECTION: Final[str] = _LLAYER + _SEP + _VALID + _S


REPORT_COLLECTION: Final[str] = _R + _S

REPORT_BLOCK_SINGLE_COLLECTION: Final[str] = _RBLOCK + _SEP + _SINGLE + _S
REPORT_BLOCK_TABLE_COLLECTION: Final[str] = _RBLOCK + _SEP + _TABLE + _S
