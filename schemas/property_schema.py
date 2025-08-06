from pydantic import BaseModel, Field
from typing import Optional
from fastapi import Form

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

    @classmethod
    def as_form(
        cls,
        title: str = Form(...),
        description: str = Form(...),
        min_price_per_day: Optional[int] = Form(None),
        max_price_per_day: Optional[int] = Form(None),
        min_price_per_month: int = Form(...),
        max_price_per_month: int = Form(...),
        deposit: int = Form(...),
        electric_price: int = Form(...),
        water_price: int = Form(...),
        service_fee: int = Form(...),
        internet_bill: Optional[int] = Form(None),
        category_id: int = Form(...),
        owner_id: int = Form(...),
    ):
        return cls(
                title=title, 
                description=description, 
                min_price_per_day=min_price_per_day, 
                max_price_per_day=max_price_per_day, 
                min_price_per_month=min_price_per_month, 
                max_price_per_month=max_price_per_month,
                deposit=deposit,
                electric_price=electric_price,
                water_price=water_price,
                service_fee=service_fee,
                internet_bill=internet_bill,
                category_id=category_id,
                owner_id=owner_id,
                )

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