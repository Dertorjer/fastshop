from typing import List, Optional
from src.catalogue.models.pydantic import CategoryModel
from src.catalogue.repository import CategoryRepository
from src.common.service.sqlalchemy import BaseSQLAlchemyService
from sqlalchemy.ext.asyncio import AsyncSession


class CategoryService(BaseSQLAlchemyService[CategoryModel]):
    def __init__(self, repository: CategoryRepository):
        super().__init__(repository=repository)

    async def get_all_categories(self) -> List[CategoryModel]:
        return await self.repository.get_all()

    async def get_category_by_id(self, category_id: int) -> Optional[CategoryModel]:
        return await self.repository.get_by_id(category_id)

    async def create_category(self, category_data: CategoryModel) -> CategoryModel:
        return await self.repository.create(category_data)

    async def update_category(self, category_id: int, category_data: CategoryModel) -> Optional[CategoryModel]:
        existing_category = await self.repository.get_by_id(category_id)
        if existing_category:
            return await self.repository.update(category_id, category_data)
        return None

    async def delete_category(self, category_id: int) -> bool:
        existing_category = await self.repository.get_by_id(category_id)
        if existing_category:
            return await self.repository.delete(category_id)
        return False
