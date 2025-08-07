from fastapi import APIRouter, Depends, Query, UploadFile, File
from typing import Optional
from schemas.favourite_property_schema import CreateFavouriteProperty, GetFavouritePropertiesDto, GetFavouritePropertiesResponse, UpdateFavouriteProperty, FavouriteProperty
from usecases.favourite_property_usecase import FavouritePropertyUseCase
from fastapi import File, UploadFile, Form
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/favourite-properties", tags=["favourite-properties"])

def get_usecase():
    return FavouritePropertyUseCase()

def get_queries(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    search: Optional[str] = Query(None)
) -> GetFavouritePropertiesDto:
    return GetFavouritePropertiesDto(skip=skip, limit=limit, search=search)

@router.get("/", response_model=GetFavouritePropertiesResponse)
def get_favourite_properties(queries: GetFavouritePropertiesDto = Depends(get_queries),usecase: FavouritePropertyUseCase = Depends(get_usecase)):
    return usecase.get_favourite_properties(queries)

@router.get("/{id}", response_model=FavouriteProperty)
def get_favourite_property(id: int, usecase: FavouritePropertyUseCase = Depends(get_usecase)):
    return usecase.get_favourite_property_by_id(id)

@router.post("/")
async def create_favourite_property(
    data: CreateFavouriteProperty,
    usecase: FavouritePropertyUseCase = Depends(get_usecase)
):
    return await usecase.create_favourite_property(data)

@router.patch("/{id}", response_model=FavouriteProperty)
def update_favourite_property(id: int, data: UpdateFavouriteProperty, usecase: FavouritePropertyUseCase = Depends(get_usecase)):
    return usecase.update_favourite_property(id, data)

@router.delete("/{id}", response_model=FavouriteProperty)
def delete_favourite_property(id: int, usecase: FavouritePropertyUseCase = Depends(get_usecase)):
    return usecase.delete_favourite_property(id)

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