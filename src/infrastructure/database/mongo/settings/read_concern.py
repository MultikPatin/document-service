from typing import Any

from pydantic import Field
from pydantic_settings import BaseSettings

from .defaults import ReadConcernDefaults


class ReadConcernSettings(BaseSettings):
    LEVEL: str = Field(
        default=ReadConcernDefaults.LEVEL,
        description="Read concern level: local, majority, linearizable",
        pattern="^(local|majority|linearizable)?$",
    )

    @property
    def client_kwargs(self) -> dict[str, Any]:
        """Returns a dictionary with parameters for creating an AsyncMongoClient
        instance.
        """
        result: dict[str, Any] = {}

        result["readConcernLevel"] = self.LEVEL

        return result
