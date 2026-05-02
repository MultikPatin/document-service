from collections.abc import Mapping
from typing import Any, Final

from pydantic_settings import SettingsConfigDict

SETTINGS_DEFAULTS: Final[Mapping[str, Any]] = {
    "env_file": ".env",
    "env_file_encoding": "utf-8",
    "extra": "ignore",
    "frozen": True,
}


def set_model_config(**kwargs: Any) -> SettingsConfigDict:  # noqa: ANN401
    for k in SETTINGS_DEFAULTS:
        if k not in kwargs:
            kwargs[k] = SETTINGS_DEFAULTS[k]
    return SettingsConfigDict(**kwargs)
