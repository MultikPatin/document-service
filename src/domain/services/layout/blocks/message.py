from typing import TYPE_CHECKING

from src.domain.models.entities import LayoutBlockMessageEntity

if TYPE_CHECKING:
    from src.domain.annotations import (
        LayoutMessageCursorFiltersType,
        LayoutMessageLimitOffsetFiltersType,
        LayoutMessagePageFiltersType,
    )
    from src.domain.models.pagination import (
        CursorResult,
        LimitOffsetResult,
        PagesResult,
    )
    from src.domain.protocols.repositories import (
        LayoutBlockMessageRepositoryProtocol,
    )


class LayoutBlockMessageService:
    def __init__(self, repo: LayoutBlockMessageRepositoryProtocol) -> None:
        self._repo = repo

    async def get(self, id_: str) -> LayoutBlockMessageEntity | None:
        return await self._repo.get(id_, return_as=LayoutBlockMessageEntity)

    # async def add(self, condition: LayoutMessageCreate) -> LayoutMessageDB:
    #     return await self._repo.add(
    #         LayoutMessageCreateDTO(
    #             **condition.model_dump(),
    #             key=generate_random_string(),
    #         ),
    #         session=session,
    #     )

    # async def update(
    #     self, id_: str, condition: LayoutMessageUpdateDTO
    # ) -> LayoutMessageDB:
    #     return await self._repo.update(id_, condition)

    async def get_all_pages(
        self, filters: LayoutMessagePageFiltersType
    ) -> PagesResult[LayoutBlockMessageEntity] | None:
        return await self._repo.get_all_pages(
            filters, return_as=LayoutBlockMessageEntity
        )

    async def get_all_limit_offset(
        self, filters: LayoutMessageLimitOffsetFiltersType
    ) -> LimitOffsetResult[LayoutBlockMessageEntity] | None:
        return await self._repo.get_all_limit_offset(
            filters, return_as=LayoutBlockMessageEntity
        )

    async def get_all_cursor(
        self, filters: LayoutMessageCursorFiltersType
    ) -> CursorResult[LayoutBlockMessageEntity] | None:
        return await self._repo.get_all_cursor(
            filters, return_as=LayoutBlockMessageEntity
        )
