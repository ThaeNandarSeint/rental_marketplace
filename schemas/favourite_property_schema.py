from pydantic import BaseModel, Field
from typing import Optional

class BaseFavouriteProperty(BaseModel):
    tenant_id: int
    property_id: int

class CreateFavouriteProperty(BaseFavouriteProperty):
    pass

class UpdateFavouriteProperty(BaseFavouriteProperty):
    pass

class FavouriteProperty(BaseFavouriteProperty):
    id: int

class GetFavouritePropertiesResponse(BaseModel):
    data: list[FavouriteProperty]
    count: int

class GetFavouritePropertiesDto(BaseModel):
    skip: int = Field(0, ge=0, description="Number of records to skip")
    limit: int = Field(10, ge=1, le=100, description="Number of records to return")
    search: Optional[str] = Field(None, description="Search keyword")