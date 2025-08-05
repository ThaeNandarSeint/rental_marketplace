from pydantic import BaseModel, Field
from typing import Optional

class BaseLocation(BaseModel):
    address: str
    city: str
    state: str
    country: str
    postal_code: str
    latitude: str
    longitude: str
    property_id: int

class CreateLocation(BaseLocation):
    pass

class UpdateLocation(BaseLocation):
    pass

class Location(BaseLocation):
    id: int

class GetLocationsResponse(BaseModel):
    data: list[Location]
    count: int

class GetLocationsDto(BaseModel):
    skip: int = Field(0, ge=0, description="Number of records to skip")
    limit: int = Field(10, ge=1, le=100, description="Number of records to return")
    search: Optional[str] = Field(None, description="Search keyword")