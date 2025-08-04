from fastapi import HTTPException
from schemas.category_schema import CreateCategory, GetCategoriesDto, UpdateCategory
from repositories.category_repository import CategoryRepository
from services.password_service import PasswordService

class CategoryService:
    def __init__(self):
        self.repository = CategoryRepository()
        self.password_service = PasswordService()

    def get_categories(self, queries: GetCategoriesDto):
        return self.repository.get_all(queries)

    def get_category(self, id: int):
        return self.repository.get_by_id(id)
    
    def get_category_by_name(self, name: str):
        return self.repository.find_one('name', name)

    def create_category(self, data: CreateCategory):
        old_category = self.get_category_by_name(data.name)
        if old_category:
            raise HTTPException(status_code=400, detail="This name already registered.")

        return self.repository.create(data)

    def update_category(self, id: int, data: UpdateCategory):
        return self.repository.update(id, data)

    def delete_category(self, id: int):
        return self.repository.delete(id)
