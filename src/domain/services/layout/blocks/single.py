from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.domain.annotations import (
        LayoutSingleCursorFiltersType,
        LayoutSingleLimitOffsetFiltersType,
        LayoutSinglePageFiltersType,
    )
    from src.domain.models.entities import LayoutBlockSingleEntity
    from src.domain.models.pagination import (
        CursorResult,
        LimitOffsetResult,
        PagesResult,
    )
    from src.domain.protocols.repositories import (
        LayoutBlockSingleRepositoryProtocol,
    )


class LayoutBlockSingleService:
    def __init__(self, repo: LayoutBlockSingleRepositoryProtocol) -> None:
        self._repo = repo

    async def get(self, id_: str) -> LayoutBlockSingleEntity | None:
        return await self._repo.get(id_, return_as=LayoutBlockSingleEntity)

    async def get_all_pages(
        self, filters: LayoutSinglePageFiltersType
    ) -> PagesResult[LayoutBlockSingleEntity] | None:
        return await self._repo.get_all_pages(
            filters, return_as=LayoutBlockSingleEntity
        )

    async def get_all_limit_offset(
        self, filters: LayoutSingleLimitOffsetFiltersType
    ) -> LimitOffsetResult[LayoutBlockSingleEntity] | None:
        return await self._repo.get_all_limit_offset(
            filters, return_as=LayoutBlockSingleEntity
        )

    async def get_all_cursor(
        self, filters: LayoutSingleCursorFiltersType
    ) -> CursorResult[LayoutBlockSingleEntity] | None:
        return await self._repo.get_all_cursor(
            filters, return_as=LayoutBlockSingleEntity
        )

    # async def get_with_layers(
    #     self,
    #     _id: str,
    #     filters: "LayersFetcherFiltersProtocol",
    #     *,
    #     session: "SessionProtocol",
    # ) -> LayoutSingleWithLayersDTO:
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
    #     return LayoutSingleWithLayersDTO.model_validate(obj)
