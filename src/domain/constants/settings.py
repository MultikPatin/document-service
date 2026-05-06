from collections.abc import Mapping
from typing import Any, Final

DEFAULT_SETTINGS_MODEL_CONFIG: Final[Mapping[str, Any]] = {
    "env_file": ".env",
    "env_file_encoding": "utf-8",
    "extra": "ignore",
    "frozen": True,
}

DEFAULT_VO_MODEL_CONFIG: Final[Mapping[str, Any]] = {
    "frozen": True,
}
