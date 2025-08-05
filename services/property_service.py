from fastapi import HTTPException
from schemas.property_schema import CreateProperty, GetPropertiesDto, UpdateProperty
from repositories.property_repository import PropertyRepository
from services.password_service import PasswordService

class PropertyService:
    def __init__(self):
        self.repository = PropertyRepository()
        self.password_service = PasswordService()

    def get_properties(self, queries: GetPropertiesDto):
        return self.repository.get_all(queries)

    def get_property(self, id: int):
        return self.repository.get_by_id(id)

    def create_property(self, data: CreateProperty):
        return self.repository.create(data)

    def update_property(self, id: int, data: UpdateProperty):
        return self.repository.update(id, data)

    def delete_property(self, id: int):
        return self.repository.delete(id)
