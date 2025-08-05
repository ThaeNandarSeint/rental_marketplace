from fastapi import APIRouter, Depends, Query 
from typing import Optional
from schemas.role_schema import CreateRole, GetRolesDto, GetRolesResponse, UpdateRole, Role
from usecases.role_usecase import RoleUseCase

router = APIRouter(prefix="/roles", tags=["roles"])

def get_usecase():
    return RoleUseCase()

def get_queries(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    search: Optional[str] = Query(None)
) -> GetRolesDto:
    return GetRolesDto(skip=skip, limit=limit, search=search)

@router.get("/", response_model=GetRolesResponse)
def get_roles(queries: GetRolesDto = Depends(get_queries),usecase: RoleUseCase = Depends(get_usecase)):
    return usecase.get_roles(queries)

@router.get("/{id}", response_model=Role)
def get_role(id: int, usecase: RoleUseCase = Depends(get_usecase)):
    return usecase.get_role_by_id(id)

@router.post("/", response_model=Role)
def create_role(data: CreateRole, usecase: RoleUseCase = Depends(get_usecase)):
    return usecase.create_role(data)

@router.patch("/{id}", response_model=Role)
def update_role(id: int, data: UpdateRole, usecase: RoleUseCase = Depends(get_usecase)):
    return usecase.update_role(id, data)

@router.delete("/{id}", response_model=Role)
def delete_role(id: int, usecase: RoleUseCase = Depends(get_usecase)):
    return usecase.delete_role(id)
