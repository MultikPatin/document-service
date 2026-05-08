from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.domain.annotations import (
        LayoutTableCursorFiltersType,
        LayoutTableLimitOffsetFiltersType,
        LayoutTablePageFiltersType,
    )
    from src.domain.models.entities import LayoutBlockTableEntity
    from src.domain.models.pagination import (
        CursorResult,
        LimitOffsetResult,
        PagesResult,
    )
    from src.domain.protocols.repositories import (
        LayoutBlockTableRepositoryProtocol,
    )


class LayoutBlockTableService:
    def __init__(self, repo: LayoutBlockTableRepositoryProtocol) -> None:
        self._repo = repo

    async def get(self, id_: str) -> LayoutBlockTableEntity | None:
        return await self._repo.get(id_, return_as=LayoutBlockTableEntity)

    async def get_all_pages(
        self, filters: LayoutTablePageFiltersType
    ) -> PagesResult[LayoutBlockTableEntity] | None:
        return await self._repo.get_all_pages(
            filters, return_as=LayoutBlockTableEntity
        )

    async def get_all_limit_offset(
        self, filters: LayoutTableLimitOffsetFiltersType
    ) -> LimitOffsetResult[LayoutBlockTableEntity] | None:
        return await self._repo.get_all_limit_offset(
            filters, return_as=LayoutBlockTableEntity
        )

    async def get_all_cursor(
        self, filters: LayoutTableCursorFiltersType
    ) -> CursorResult[LayoutBlockTableEntity] | None:
        return await self._repo.get_all_cursor(
            filters, return_as=LayoutBlockTableEntity
        )

    # async def get_with_layers(
    #     self,
    #     _id: str,
    #     filters: "LayersFetcherFiltersProtocol",
    #     *,
    #     session: "SessionProtocol",
    # ) -> LayoutTableWithLayersDTO:
    #     instance = await self._repo.get(_id, session=session)
    #     obj = instance.model_dump()
    #
    #     await self._fetcher.fetch_block(
    #         obj,  # type: ignore
    #         session=session,
    #         layers=filters.layers,
    #         in_place=True,
    #     )
    #
    #     return LayoutTableWithLayersDTO.model_validate(obj)
