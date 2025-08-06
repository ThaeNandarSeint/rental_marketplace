from fastapi import APIRouter, Depends, Query 
from typing import Optional
from schemas.property_file_schema import GetPropertyFilesDto, GetPropertyFilesResponse, PropertyFile
from usecases.property_file_usecase import PropertyFileUseCase

router = APIRouter(prefix="/property-files", tags=["property-files"])

def get_usecase():
    return PropertyFileUseCase()

def get_queries(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    search: Optional[str] = Query(None)
) -> GetPropertyFilesDto:
    return GetPropertyFilesDto(skip=skip, limit=limit, search=search)

@router.get("/", response_model=GetPropertyFilesResponse)
def get_property_files(queries: GetPropertyFilesDto = Depends(get_queries),usecase: PropertyFileUseCase = Depends(get_usecase)):
    return usecase.get_property_files(queries)

@router.get("/{id}", response_model=PropertyFile)
def get_property_file(id: int, usecase: PropertyFileUseCase = Depends(get_usecase)):
    return usecase.get_property_file_by_id(id)

@router.delete("/{id}", response_model=PropertyFile)
def delete_property_file(id: int, usecase: PropertyFileUseCase = Depends(get_usecase)):
    return usecase.delete_property_file(id)
