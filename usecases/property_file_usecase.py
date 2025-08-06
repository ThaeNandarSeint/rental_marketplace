from fastapi import HTTPException
from services.property_file_service import PropertyFileService
from schemas.property_file_schema import GetPropertyFilesDto

class PropertyFileUseCase:
    def __init__(self):
        self.service = PropertyFileService()

    def get_property_files(self, queries: GetPropertyFilesDto):
        return self.service.get_property_files(queries)

    def get_property_file_by_id(self, id: int):
        data = self.service.get_property_file(id)
        if not data:
            raise HTTPException(status_code=400, detail="PropertyFile not found")
        return data

    def delete_property_file(self, id: int):
        return self.service.delete_property_file(id)
