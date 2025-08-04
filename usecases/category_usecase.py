from fastapi import HTTPException
from services.category_service import CategoryService
from schemas.category_schema import CreateCategory, GetCategoriesDto, UpdateCategory

class CategoryUseCase:
    def __init__(self):
        self.service = CategoryService()

    def get_categories(self, queries: GetCategoriesDto):
        return self.service.get_categories(queries)

    def get_category_by_id(self, id: int):
        data = self.service.get_category(id)
        if not data:
            raise HTTPException(status_code=400, detail="Category not found")
        return data

    def create_category(self, data: CreateCategory):
        return self.service.create_category(data)

    def update_category(self, id: int, data: UpdateCategory):
        return self.service.update_category(id, data)

    def delete_category(self, id: int):
        return self.service.delete_category(id)
