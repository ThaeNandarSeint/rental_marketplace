from schemas.location_schema import CreateLocation, GetLocationsDto, UpdateLocation
from repositories.location_repository import LocationRepository
from services.password_service import PasswordService

class LocationService:
    def __init__(self):
        self.repository = LocationRepository()
        self.password_service = PasswordService()

    def get_locations(self, queries: GetLocationsDto):
        return self.repository.get_all(queries)

    def get_location(self, id: int):
        return self.repository.get_by_id(id)

    def create_location(self, data: CreateLocation):
        return self.repository.create(data)

    def update_location(self, id: int, data: UpdateLocation):
        return self.repository.update(id, data)

    def delete_location(self, id: int):
        return self.repository.delete(id)
