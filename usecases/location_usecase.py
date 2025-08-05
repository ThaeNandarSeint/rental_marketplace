from fastapi import HTTPException
from services.location_service import LocationService
from schemas.location_schema import CreateLocation, GetLocationsDto, UpdateLocation

class LocationUseCase:
    def __init__(self):
        self.service = LocationService()

    def get_locations(self, queries: GetLocationsDto):
        return self.service.get_locations(queries)

    def get_location_by_id(self, id: int):
        data = self.service.get_location(id)
        if not data:
            raise HTTPException(status_code=400, detail="Location not found")
        return data

    def create_location(self, data: CreateLocation):
        return self.service.create_location(data)

    def update_location(self, id: int, data: UpdateLocation):
        return self.service.update_location(id, data)

    def delete_location(self, id: int):
        return self.service.delete_location(id)
