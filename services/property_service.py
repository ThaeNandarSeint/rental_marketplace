from fastapi import UploadFile
from schemas.property_schema import CreateProperty, GetPropertiesDto, UpdateProperty
from repositories.property_repository import PropertyRepository
from services.password_service import PasswordService
from services.property_file_service import PropertyFileService

class PropertyService:
    def __init__(self):
        self.repository = PropertyRepository()
        self.password_service = PasswordService()
        self.property_file_service = PropertyFileService()

    def get_properties(self, queries: GetPropertiesDto):
        return self.repository.get_all(queries)

    def get_property(self, id: int):
        return self.repository.get_by_id(id)

    async def create_property(self, data: CreateProperty, file: UploadFile):
        property = self.repository.create(data)
        await self.property_file_service.create_property_file(file, property.id)
        return property

    def update_property(self, id: int, data: UpdateProperty):
        return self.repository.update(id, data)

    def delete_property(self, id: int):
        return self.repository.delete(id)
