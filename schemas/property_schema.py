from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class BaseProperty(BaseModel):
    title: str
    description: str
    min_price_per_day: Optional[int] = None
    max_price_per_day: Optional[int] = None
    min_price_per_month: int
    max_price_per_month: int
    deposit: int
    electric_price: int
    water_price: int
    service_fee: int
    internet_bill: Optional[int] = None
    category_id: int
    owner_id: int

class CreateProperty(BaseProperty):
    pass

class UpdateProperty(BaseProperty):
    pass

class Property(BaseProperty):
    id: int

class GetPropertiesResponse(BaseModel):
    data: list[Property]
    count: int

class GetPropertiesDto(BaseModel):
    skip: int = Field(0, ge=0, description="Number of records to skip")
    limit: int = Field(10, ge=1, le=100, description="Number of records to return")
    search: Optional[str] = Field(None, description="Search keyword")