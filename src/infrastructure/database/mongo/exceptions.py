class MongoAdapterError(Exception):
    def __init__(self, message: str, /) -> None:
        super().__init__(message)


class InvalidMongoIDError(MongoAdapterError):
    def __init__(self, value: str, /) -> None:
        message = (
            f"Invalid ID value: {value}, type: {type(value)}"
            f"Expected Bson ObjectID in string format. "
            f"It must be a 12-byte input or a 24-character hex string."
        )
        super().__init__(message)
