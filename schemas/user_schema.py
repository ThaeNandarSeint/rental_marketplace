from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class BaseUser(BaseModel):
    name: str
    email: EmailStr
    password: str

class CreateUser(BaseUser):
    pass

class UpdateUser(BaseUser):
    pass

class User(BaseUser):
    id: int

class GetUsersResponse(BaseModel):
    data: list[User]
    count: int

class GetUsersDto(BaseModel):
    skip: int = Field(0, ge=0, description="Number of records to skip")
    limit: int = Field(10, ge=1, le=100, description="Number of records to return")
    search: Optional[str] = Field(None, description="Search keyword")