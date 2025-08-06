from fastapi import UploadFile
from schemas.property_file_schema import CreatePropertyFile, GetPropertyFilesDto, UpdatePropertyFile
from repositories.property_file_repository import PropertyFileRepository
from services.file_service import FileService

class PropertyFileService:
    def __init__(self):
        self.repository = PropertyFileRepository()
        self.file_service = FileService()

    def get_property_files(self, queries: GetPropertyFilesDto):
        return self.repository.get_all(queries)

    def get_property_file(self, id: int):
        return self.repository.get_by_id(id)
    
    async def create_property_file(self, file: UploadFile, property_id: int):
        result = await self.file_service.upload_image(file, '/properties')
        data = CreatePropertyFile(**{
            "name": result['public_id'],
            "url": result['secure_url'],
            "type": 'image',
            "property_id": property_id
        })
        return self.repository.create(data)

    def update_property_file(self, id: int, data: UpdatePropertyFile):
        return self.repository.update(id, data)

    def delete_property_file(self, id: int):
        return self.repository.delete(id)
