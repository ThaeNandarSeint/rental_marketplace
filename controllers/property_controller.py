from fastapi import APIRouter, Depends, Query, UploadFile, File
from typing import Optional
from schemas.property_schema import CreateProperty, GetPropertiesDto, GetPropertiesResponse, UpdateProperty, Property
from usecases.property_usecase import PropertyUseCase
from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/properties", tags=["properties"])

def get_usecase():
    return PropertyUseCase()

def get_queries(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    search: Optional[str] = Query(None)
) -> GetPropertiesDto:
    return GetPropertiesDto(skip=skip, limit=limit, search=search)

@router.get("/", response_model=GetPropertiesResponse)
def get_properties(queries: GetPropertiesDto = Depends(get_queries),usecase: PropertyUseCase = Depends(get_usecase)):
    return usecase.get_properties(queries)

@router.get("/{id}", response_model=Property)
def get_property(id: int, usecase: PropertyUseCase = Depends(get_usecase)):
    return usecase.get_property_by_id(id)

@router.post("/")
async def create_property(
    data: CreateProperty = Depends(CreateProperty.as_form),
    file: UploadFile = File(...),
    usecase: PropertyUseCase = Depends(get_usecase)
):
    return await usecase.create_property(data, file)

@router.patch("/{id}", response_model=Property)
def update_property(id: int, data: UpdateProperty, usecase: PropertyUseCase = Depends(get_usecase)):
    return usecase.update_property(id, data)

@router.delete("/{id}", response_model=Property)
def delete_property(id: int, usecase: PropertyUseCase = Depends(get_usecase)):
    return usecase.delete_property(id)

@router.post("/upload")
async def upload_file(
    name: str = Form(...),
    age: int = Form(...),
    file: UploadFile = File(...)
):
    return JSONResponse({
        "filename": file.filename,
        "content_type": file.content_type,
        "name": name,
        "age": age
    })