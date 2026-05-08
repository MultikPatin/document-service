from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.domain.models.entities import LayoutLayerDefaultEntity
    from src.domain.protocols.repositories import (
        LayoutLayerDefaultRepositoryProtocol,
    )


class LayoutLayerDefaultService:
    def __init__(self, repo: LayoutLayerDefaultRepositoryProtocol) -> None:
        self._repo = repo

    async def get(self, id_: str) -> LayoutLayerDefaultEntity | None:
        return await self._repo.get(id_, return_as=LayoutLayerDefaultEntity)

    # async def add(
    #     self, condition: "LayoutDefaultCreateDTO"
    # ) -> "LayoutDefaultDB":
    #     return await self._repo.add(condition)
    #
    # async def update(
    #     self,
    #     _id: str,
    #     condition: "LayoutDefaultUpdateDTO",
    #     *,
    # ) -> "LayoutDefaultDB":
    #     return await self._repo.update(_id, condition)
    #
    # async def delete(self, id_: str) -> str:
    #     return await self._repo.delete(id_)
