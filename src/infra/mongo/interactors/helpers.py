from typing import TYPE_CHECKING, Any

from src.infra.mongo.enums import KeyEnum
from src.infra.mongo.utils import to_id

from .base import BaseInteractor

if TYPE_CHECKING:
    from beanie import Document

    from src.infra.mongo.annotations import QueryConditionsType


class CountByConditions[D: Document](BaseInteractor[D]):
    async def __call__(
        self,
        conditions: QueryConditionsType,
        *,
        ignore_cache: bool = False,
        fetch_links: bool = False,
        **pymongo_kwargs: Any,  # noqa: ANN401
    ) -> int:
        return await self._document.find(
            *conditions,
            session=self._session,
            ignore_cache=ignore_cache,
            fetch_links=fetch_links,
            **pymongo_kwargs,
        ).count()


class ExistsByHash[D: Document](BaseInteractor[D]):
    async def __call__(
        self,
        hash_string: str,
        *,
        ignore_cache: bool = False,
        **pymongo_kwargs: Any,  # noqa: ANN401
    ) -> bool:
        return await self._document.find_one(
            {"hash": hash_string},
            session=self._session,
            ignore_cache=ignore_cache,
            **pymongo_kwargs,
        ).exists()


class ExistsByID[D: Document](BaseInteractor[D]):
    async def __call__(
        self,
        document_id: str,
        *,
        ignore_cache: bool = False,
        **pymongo_kwargs: Any,  # noqa: ANN401
    ) -> bool:
        return await self._document.find_one(
            {KeyEnum.id: to_id(document_id)},
            session=self._session,
            ignore_cache=ignore_cache,
            **pymongo_kwargs,
        ).exists()
