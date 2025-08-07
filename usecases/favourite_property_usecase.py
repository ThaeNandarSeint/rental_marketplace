from fastapi import HTTPException, UploadFile
from services.favourite_property_service import FavouritePropertyService
from schemas.favourite_property_schema import CreateFavouriteProperty, GetFavouritePropertiesDto, UpdateFavouriteProperty

class FavouritePropertyUseCase:
    def __init__(self):
        self.service = FavouritePropertyService()

    def get_favourite_properties(self, queries: GetFavouritePropertiesDto):
        return self.service.get_favourite_properties(queries)

    def get_favourite_property_by_id(self, id: int):
        data = self.service.get_favourite_property(id)
        if not data:
            raise HTTPException(status_code=400, detail="Favourite Property not found")
        return data

    def create_favourite_property(self, data: CreateFavouriteProperty):
        return self.service.create_favourite_property(data)

    def update_favourite_property(self, id: int, data: UpdateFavouriteProperty):
        return self.service.update_favourite_property(id, data)

    def delete_favourite_property(self, id: int):
        return self.service.delete_favourite_property(id)
