from pydantic import BaseModel, Field
from typing import Optional
from schemas.user_schema import BaseUser
from schemas.role_schema import BaseRole

class BaseAdmin(BaseModel):
    user_id: int
    role_id: int

class AdminUser(BaseUser):
    type: Optional[str]

class CreateAdmin(BaseModel):
    user: AdminUser
    role_id: int

class UpdateAdmin(BaseAdmin):
    pass

class Admin(BaseAdmin):
    id: int
    user: Optional[BaseUser]
    role: Optional[BaseRole]

class GetAdminsResponse(BaseModel):
    data: list[Admin]
    count: int

class GetAdminsDto(BaseModel):
    skip: int = Field(0, ge=0, description="Number of records to skip")
    limit: int = Field(10, ge=1, le=100, description="Number of records to return")
    search: Optional[str] = Field(None, description="Search keyword")