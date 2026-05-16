from src.api.core.settings.api_mounted import Settings as MountedSettings
from src.domain.utils import settings_model_config

from .constants import ENV_PREFIX


class Settings(MountedSettings):
    model_config = settings_model_config(env_prefix=ENV_PREFIX)
