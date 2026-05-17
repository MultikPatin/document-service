from typing import Final

from src.api.storage.constants import API_ENV_PREFIX

_VERSION: Final[str] = "V3_"

ENV_PREFIX: Final[str] = API_ENV_PREFIX + _VERSION
