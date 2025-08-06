from pydantic import BaseModel, Field
from typing import Optional

class BasePropertyFile(BaseModel):
    name: str
    url: str
    type: str
    property_id: int

class CreatePropertyFile(BasePropertyFile):
    pass

class UpdatePropertyFile(BasePropertyFile):
    pass

class PropertyFile(BasePropertyFile):
    id: int

class GetPropertyFilesResponse(BaseModel):
    data: list[PropertyFile]
    count: int

class GetPropertyFilesDto(BaseModel):
    skip: int = Field(0, ge=0, description="Number of records to skip")
    limit: int = Field(10, ge=1, le=100, description="Number of records to return")
    search: Optional[str] = Field(None, description="Search keyword")