from fastapi import UploadFile
from schemas.favourite_property_schema import CreateFavouriteProperty, GetFavouritePropertiesDto, UpdateFavouriteProperty
from repositories.favourite_property_repository import FavouritePropertyRepository
from services.password_service import PasswordService

class FavouritePropertyService:
    def __init__(self):
        self.repository = FavouritePropertyRepository()

    def get_favourite_properties(self, queries: GetFavouritePropertiesDto):
        return self.repository.get_all(queries)

    def get_favourite_property(self, id: int):
        return self.repository.get_by_id(id)

    async def create_favourite_property(self, data: CreateFavouriteProperty):
        return self.repository.create(data)

    def update_favourite_property(self, id: int, data: UpdateFavouriteProperty):
        return self.repository.update(id, data)

    def delete_favourite_property(self, id: int):
        return self.repository.delete(id)
