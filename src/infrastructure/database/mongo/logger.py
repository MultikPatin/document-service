from typing import Final, final


@final
class LoggerNames:
    MAIN: Final[str] = "mongodb"
    SEPARATOR: Final[str] = "."
    INIT: Final[str] = "init"

    @classmethod
    def _root(cls) -> str:
        return cls.MAIN + cls.SEPARATOR

    @classmethod
    def init(cls) -> str:
        return cls._root() + cls.INIT
