from fastapi import APIRouter, Depends, Query 
from typing import Optional
from schemas.owner_schema import CreateOwner, GetOwnersDto, GetOwnersResponse, UpdateOwner, Owner
from usecases.owner_usecase import OwnerUseCase

router = APIRouter(prefix="/owners", tags=["owners"])

def get_usecase():
    return OwnerUseCase()

def get_queries(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    search: Optional[str] = Query(None)
) -> GetOwnersDto:
    return GetOwnersDto(skip=skip, limit=limit, search=search)

@router.get("/", response_model=GetOwnersResponse)
def get_owners(queries: GetOwnersDto = Depends(get_queries),usecase: OwnerUseCase = Depends(get_usecase)):
    return usecase.get_owners(queries)

@router.get("/{id}", response_model=Owner)
def get_owner(id: int, usecase: OwnerUseCase = Depends(get_usecase)):
    return usecase.get_owner_by_id(id)

@router.post("/", response_model=Owner)
def create_owner(data: CreateOwner, usecase: OwnerUseCase = Depends(get_usecase)):
    return usecase.create_owner(data)

@router.patch("/{id}", response_model=Owner)
def update_owner(id: int, data: UpdateOwner, usecase: OwnerUseCase = Depends(get_usecase)):
    return usecase.update_owner(id, data)

@router.delete("/{id}", response_model=Owner)
def delete_owner(id: int, usecase: OwnerUseCase = Depends(get_usecase)):
    return usecase.delete_owner(id)
