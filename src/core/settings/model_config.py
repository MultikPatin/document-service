from typing import Any

from pydantic_settings import SettingsConfigDict

from .constants import MODEL_CONFIG_DEFAULTS


def model_config(**kwargs: Any) -> SettingsConfigDict:  # noqa: ANN401
    """Creates a Pydantic SettingsConfigDict with default values.

    This function takes optional keyword arguments and merges them with
    default configuration values defined in MODEL_CONFIG_DEFAULTS.
    If a key is not provided in kwargs, its default value from
    MODEL_CONFIG_DEFAULTS will be used. The resulting dictionary is used to
    create a SettingsConfigDict.

    Args:
        **kwargs: Arbitrary keyword arguments that will be passed to
                  SettingsConfigDict. Common parameters include:
                  - env_file: Path to environment file (default: ".env")
                  - env_file_encoding: Encoding of environment file
                    (default: "utf-8")
                  - env_nested_delimiter: Delimiter for nested environment
                    variables (default: "__")
                  - extra: How to handle extra fields (default: "ignore")
                  - frozen: Whether the model should be frozen/immutable
                    (default: True)

    Returns:
        SettingsConfigDict: A configuration dictionary for Pydantic
                          settings model

    Example:
        >>> config = model_config(env_file=".env.prod", extra="allow")
        >>> print(config)
        SettingsConfigDict(env_file='.env.prod',
                          env_file_encoding='utf-8',
                          env_nested_delimiter='__',
                          extra='allow',
                          frozen=True)
    """
    for k in MODEL_CONFIG_DEFAULTS:
        if k not in kwargs:
            kwargs[k] = MODEL_CONFIG_DEFAULTS[k]
    return SettingsConfigDict(**kwargs)
