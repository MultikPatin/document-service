from src.infrastructure.errors import InfrastructureError


class MongoError(InfrastructureError):
    pass


class StartSessionError(InfrastructureError):
    def __init__(self) -> None:
        message = "Couldn't start session"
        super().__init__(message)


class InvalidMongoIDError(MongoError):
    def __init__(self, value: str, /) -> None:
        message = (
            f"Invalid ID value: {value}, type: {type(value)}"
            f"Expected Bson ObjectID in string format. "
            f"It must be a 12-byte input or a 24-character hex string."
        )
        super().__init__(message)
