from typing import Any, Final, final

from libs.core.constants import ModelConfigDefaults


@final
class BaseDefaults(ModelConfigDefaults):
    ENV_PREFIX: Final[str] = "MONGODB_"

    @classmethod
    def model_config(cls) -> dict[str, Any]:
        c = super().model_config()
        c.update({"env_prefix": cls.ENV_PREFIX})
        return c
