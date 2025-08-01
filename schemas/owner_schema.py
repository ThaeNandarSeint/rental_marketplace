from pydantic import BaseModel, Field
from typing import Optional
from schemas.user_schema import BaseUser

class BaseOwner(BaseModel):
    user_id: int

class CreateOwner(BaseOwner):
    pass

class UpdateOwner(BaseOwner):
    pass

class Owner(BaseOwner):
    id: int
    user: Optional[BaseUser]

class GetOwnersResponse(BaseModel):
    data: list[Owner]
    count: int

class GetOwnersDto(BaseModel):
    skip: int = Field(0, ge=0, description="Number of records to skip")
    limit: int = Field(10, ge=1, le=100, description="Number of records to return")
    search: Optional[str] = Field(None, description="Search keyword")