from typing import Any

from pydantic import ConfigDict
from pydantic_settings import SettingsConfigDict

from src.domain.constants import (
    DEFAULT_SETTINGS_MODEL_CONFIG,
    DEFAULT_VO_MODEL_CONFIG,
)


def settings_model_config(**kwargs: Any) -> SettingsConfigDict:  # noqa: ANN401
    for k in DEFAULT_SETTINGS_MODEL_CONFIG:
        if k not in kwargs:
            kwargs[k] = DEFAULT_SETTINGS_MODEL_CONFIG[k]
    return SettingsConfigDict(**kwargs)


def vo_model_config(**kwargs: Any) -> ConfigDict:  # noqa: ANN401
    for k in DEFAULT_VO_MODEL_CONFIG:
        if k not in kwargs:
            kwargs[k] = DEFAULT_VO_MODEL_CONFIG[k]
    return ConfigDict(**kwargs)
