from src.api.core.settings.api import MountSettings
from src.domain.utils import settings_model_config

from .constants import ENV_PREFIX


class Settings(MountSettings):
    model_config = settings_model_config(env_prefix=ENV_PREFIX)
