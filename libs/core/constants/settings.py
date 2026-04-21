from typing import Any, Final, Literal


class ModelConfigDefaults:
    ENV_FILE: Final[str] = ".env"
    ENV_FILE_ENCODING: Final[str] = "utf-8"
    ENV_NESTED_DELIMITER: Final[str] = "__"
    EXTRA: Final[Literal["allow", "ignore", "forbid"]] = "ignore"
    FROZEN: Final[bool] = True

    @classmethod
    def model_config(cls) -> dict[str, Any]:
        return {
            "env_file": cls.ENV_FILE,
            "env_file_encoding": cls.ENV_FILE_ENCODING,
            "env_nested_delimiter": cls.ENV_NESTED_DELIMITER,
            "extra": cls.EXTRA,
            "frozen": cls.FROZEN,
        }
