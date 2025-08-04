from pydantic import BaseModel, Field
from typing import Optional

class BaseCategory(BaseModel):
    name: str

class CreateCategory(BaseCategory):
    pass

class UpdateCategory(BaseCategory):
    pass

class Category(BaseCategory):
    id: int

class GetCategoriesResponse(BaseModel):
    data: list[Category]
    count: int

class GetCategoriesDto(BaseModel):
    skip: int = Field(0, ge=0, description="Number of records to skip")
    limit: int = Field(10, ge=1, le=100, description="Number of records to return")
    search: Optional[str] = Field(None, description="Search keyword")