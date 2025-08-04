from pydantic import BaseModel, Field
from typing import Optional

class BaseRole(BaseModel):
    name: str

class CreateRole(BaseRole):
    pass

class UpdateRole(BaseRole):
    pass

class Role(BaseRole):
    id: int

class GetRolesResponse(BaseModel):
    data: list[Role]
    count: int

class GetRolesDto(BaseModel):
    skip: int = Field(0, ge=0, description="Number of records to skip")
    limit: int = Field(10, ge=1, le=100, description="Number of records to return")
    search: Optional[str] = Field(None, description="Search keyword")