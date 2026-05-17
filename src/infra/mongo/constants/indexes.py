from typing import Final

_SEP: Final[str] = "_"

_INDEX: Final[str] = _SEP + "idx"
_UNIQUE: Final[str] = _SEP + "unique"

_ASCENDING: Final[str] = _INDEX + _SEP + "ASCENDING"
_DESCENDING: Final[str] = _INDEX + _SEP + "DESCENDING"
_HASHED: Final[str] = _INDEX + _SEP + "HASHED"

_HASH: Final[str] = "hash"
_KEY: Final[str] = "key"
_VERSION: Final[str] = "version"
_KEY_VERSION: Final[str] = _KEY + _SEP + _VERSION

INDEX_HASH_HASHED: Final[str] = _HASH + _UNIQUE + _HASHED
INDEX_KEY_VERSION_DESCENDING: Final[str] = _KEY_VERSION + _UNIQUE + _DESCENDING
