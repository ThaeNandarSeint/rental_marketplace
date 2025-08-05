from fastapi import APIRouter, Depends, Query 
from typing import Optional
from schemas.category_schema import CreateCategory, GetCategoriesDto, GetCategoriesResponse, UpdateCategory, Category
from usecases.category_usecase import CategoryUseCase

router = APIRouter(prefix="/categories", tags=["categories"])

def get_usecase():
    return CategoryUseCase()

def get_queries(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    search: Optional[str] = Query(None)
) -> GetCategoriesDto:
    return GetCategoriesDto(skip=skip, limit=limit, search=search)

@router.get("/", response_model=GetCategoriesResponse)
def get_categories(queries: GetCategoriesDto = Depends(get_queries),usecase: CategoryUseCase = Depends(get_usecase)):
    return usecase.get_categories(queries)

@router.get("/{id}", response_model=Category)
def get_category(id: int, usecase: CategoryUseCase = Depends(get_usecase)):
    return usecase.get_category_by_id(id)

@router.post("/", response_model=Category)
def create_category(data: CreateCategory, usecase: CategoryUseCase = Depends(get_usecase)):
    return usecase.create_category(data)

@router.patch("/{id}", response_model=Category)
def update_category(id: int, data: UpdateCategory, usecase: CategoryUseCase = Depends(get_usecase)):
    return usecase.update_category(id, data)

@router.delete("/{id}", response_model=Category)
def delete_category(id: int, usecase: CategoryUseCase = Depends(get_usecase)):
    return usecase.delete_category(id)
