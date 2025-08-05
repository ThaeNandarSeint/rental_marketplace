from fastapi import APIRouter, Depends, Query 
from typing import Optional
from schemas.admin_schema import (Admin, CreateAdmin, GetAdminsDto,
    GetAdminsResponse, UpdateAdmin)
from usecases.admin_usecase import AdminUseCase

router = APIRouter(prefix="/admins", tags=["admins"])

def get_usecase():
    return AdminUseCase()

def get_queries(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    search: Optional[str] = Query(None)
) -> GetAdminsDto:
    return GetAdminsDto(skip=skip, limit=limit, search=search)

@router.get("/", response_model=GetAdminsResponse)
def get_admins(queries: GetAdminsDto = Depends(get_queries),usecase: AdminUseCase = Depends(get_usecase)):
    return usecase.get_admins(queries)

@router.get("/{id}", response_model=Admin)
def get_admin(id: int, usecase: AdminUseCase = Depends(get_usecase)):
    return usecase.get_admin_by_id(id)

@router.post("/", response_model=Admin)
def create_admin(data: CreateAdmin, usecase: AdminUseCase = Depends(get_usecase)):
    return usecase.create_admin(data)

@router.patch("/{id}", response_model=Admin)
def update_admin(id: int, data: UpdateAdmin, usecase: AdminUseCase = Depends(get_usecase)):
    return usecase.update_admin(id, data)

@router.delete("/{id}", response_model=Admin)
def delete_admin(id: int, usecase: AdminUseCase = Depends(get_usecase)):
    return usecase.delete_admin(id)
