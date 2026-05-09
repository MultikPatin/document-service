from typing import Any

from src.infrastructure.errors import InfrastructureError


class MongoError(InfrastructureError):
    pass


class StartSessionError(InfrastructureError):
    def __init__(self) -> None:
        message = "Couldn't start session"
        super().__init__(message)


class InvalidIDError(MongoError):
    def __init__(self, value: str) -> None:
        message = (
            f"Invalid ID value: {value}, type: {type(value)}"
            f"Expected Bson ObjectID in string format. "
            f"It must be a 12-byte input or a 24-character hex string."
        )
        super().__init__(message)


class InvalidSortError(MongoError):
    def __init__(self, value: Any) -> None:  # noqa: ANN401
        message = (
            f"Sorting by '{value}' of type: '{type(value)}' is not allowed"
        )
        super().__init__(message)
