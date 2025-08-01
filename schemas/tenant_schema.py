from pydantic import BaseModel, Field
from typing import Optional
from schemas.user_schema import BaseUser

class BaseTenant(BaseModel):
    user_id: int

class CreateTenant(BaseTenant):
    pass

class UpdateTenant(BaseTenant):
    pass

class Tenant(BaseTenant):
    id: int
    user: Optional[BaseUser]

class GetTenantsResponse(BaseModel):
    data: list[Tenant]
    count: int

class GetTenantsDto(BaseModel):
    skip: int = Field(0, ge=0, description="Number of records to skip")
    limit: int = Field(10, ge=1, le=100, description="Number of records to return")
    search: Optional[str] = Field(None, description="Search keyword")