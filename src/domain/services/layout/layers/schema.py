from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.domain.models.entities import LayoutLayerSchemaEntity
    from src.domain.protocols.repositories import (
        LayoutLayerSchemaRepositoryProtocol,
    )


class LayoutLayerSchemaService:
    def __init__(self, repo: LayoutLayerSchemaRepositoryProtocol) -> None:
        self._repo = repo

    async def get(self, id_: str) -> LayoutLayerSchemaEntity | None:
        return await self._repo.get(id_, return_as=LayoutLayerSchemaEntity)

    # async def add(
    #     self, condition: "LayoutSchemaCreateDTO"
    # ) -> "LayoutSchemaDB":
    #     return await self._repo.add(condition)
    #
    # async def update(
    #     self,
    #     _id: str,
    #     condition: "LayoutSchemaUpdateDTO",
    #     *,
    # ) -> "LayoutSchemaDB":
    #     return await self._repo.update(_id, condition)
    #
    # async def delete(self, id_: str) -> str:
    #     return await self._repo.delete(id_)
