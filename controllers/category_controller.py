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
def get_Categorys(queries: GetCategoriesDto = Depends(get_queries),usecase: CategoryUseCase = Depends(get_usecase)):
    return usecase.get_Categorys(queries)

@router.get("/{id}", response_model=Category)
def get_Category(id: int, usecase: CategoryUseCase = Depends(get_usecase)):
    return usecase.get_Category_by_id(id)

@router.post("/", response_model=Category)
def create_Category(Category: CreateCategory, usecase: CategoryUseCase = Depends(get_usecase)):
    return usecase.create_Category(Category)

@router.patch("/{id}", response_model=Category)
def update_Category(id: int, Category: UpdateCategory, usecase: CategoryUseCase = Depends(get_usecase)):
    return usecase.update_Category(id, Category)

@router.delete("/{id}", response_model=Category)
def delete_Category(id: int, usecase: CategoryUseCase = Depends(get_usecase)):
    return usecase.delete_Category(id)
