from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from schemas.user_schema import BaseUser

class BaseAdmin(BaseModel):
    user_id: int

class CreateAdmin(BaseUser):
    type: Optional[str] = None

class UpdateAdmin(BaseAdmin):
    pass

class Admin(BaseAdmin):
    id: int
    user: Optional[BaseUser]

class GetAdminsResponse(BaseModel):
    data: list[Admin]
    count: int

class GetAdminsDto(BaseModel):
    skip: int = Field(0, ge=0, description="Number of records to skip")
    limit: int = Field(10, ge=1, le=100, description="Number of records to return")
    search: Optional[str] = Field(None, description="Search keyword")