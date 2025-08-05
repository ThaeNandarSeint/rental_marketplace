from fastapi import HTTPException
from services.property_service import PropertyService
from schemas.property_schema import CreateProperty, GetPropertiesDto, UpdateProperty

class PropertyUseCase:
    def __init__(self):
        self.service = PropertyService()

    def get_properties(self, queries: GetPropertiesDto):
        return self.service.get_properties(queries)

    def get_property_by_id(self, id: int):
        data = self.service.get_property(id)
        if not data:
            raise HTTPException(status_code=400, detail="Property not found")
        return data

    def create_property(self, data: CreateProperty):
        return self.service.create_property(data)

    def update_property(self, id: int, data: UpdateProperty):
        return self.service.update_property(id, data)

    def delete_property(self, id: int):
        return self.service.delete_property(id)
