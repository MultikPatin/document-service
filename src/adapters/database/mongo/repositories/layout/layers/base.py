from typing import TYPE_CHECKING

from libs.core.utils import get_md5hash
from libs.mongo.mixins.repository_methods import (
    AddMixin,
    # UpdateMixin,
    # DeleteWithRefCountMixin,
    DecRefCountMixin,
    GetByHashMixin,
    GetByIDsMixin,
    GetMixin,
    IncRefCountMixin,
)
from pydantic import BaseModel

if TYPE_CHECKING:
    from pymongo.asynchronous.client_session import AsyncClientSession


class ModelWithHash(BaseModel):
    hash: str | None = None


class _Repository(
    GetMixin,
    GetByIDsMixin,
    GetByHashMixin,
    AddMixin,
    # UpdateMixin,
    # DeleteWithRefCountMixin,
    DecRefCountMixin,
    IncRefCountMixin,
):
    async def add_by_hash[ReturnSchema, CreateSchema: ModelWithHash](
        self,
        condition: CreateSchema,
        *,
        session: AsyncClientSession,
        return_as: type[ReturnSchema],
    ) -> ReturnSchema:
        exclude = {"hash", "id", "ref_count"}
        hash_string = get_md5hash(condition.model_dump(exclude=exclude))

        result = await self.get_by_hash(
            hash_string, session=session, return_as=return_as
        )

        if result is None:
            condition.hash = hash_string
            result = await super().add(
                condition, session=session, return_as=return_as
            )

        return result
