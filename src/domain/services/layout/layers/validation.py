from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.domain.models.entities import LayoutLayerValidationEntity
    from src.domain.protocols.repositories import (
        LayoutLayerValidationRepositoryProtocol,
    )


class LayoutLayerValidationService:
    def __init__(self, repo: LayoutLayerValidationRepositoryProtocol) -> None:
        self._repo = repo

    async def get(self, id_: str) -> LayoutLayerValidationEntity | None:
        return await self._repo.get(id_, return_as=LayoutLayerValidationEntity)

    # async def add(
    #     self, condition: "LayoutValidationCreateDTO"
    # ) -> "LayoutValidationDB":
    #     return await self._repo.add(condition)
    #
    # async def update(
    #     self,
    #     _id: str,
    #     condition: "LayoutValidationUpdateDTO",
    #     *,
    # ) -> "LayoutValidationDB":
    #     return await self._repo.update(_id, condition)
    #
    # async def delete(self, id_: str) -> str:
    #     return await self._repo.delete(id_)
