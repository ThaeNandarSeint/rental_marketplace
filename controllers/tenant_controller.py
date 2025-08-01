from fastapi import APIRouter, Depends, Query 
from typing import Optional
from schemas.tenant_schema import CreateTenant, GetTenantsDto, GetTenantsResponse, UpdateTenant, Tenant
from usecases.tenant_usecase import TenantUseCase

router = APIRouter(prefix="/tenants", tags=["tenants"])

def get_usecase():
    return TenantUseCase()

def get_queries(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    search: Optional[str] = Query(None)
) -> GetTenantsDto:
    return GetTenantsDto(skip=skip, limit=limit, search=search)

@router.get("/", response_model=GetTenantsResponse)
def get_tenants(queries: GetTenantsDto = Depends(get_queries),usecase: TenantUseCase = Depends(get_usecase)):
    return usecase.get_tenants(queries)

@router.get("/{id}", response_model=Tenant)
def get_tenant(id: int, usecase: TenantUseCase = Depends(get_usecase)):
    return usecase.get_tenant_by_id(id)

@router.post("/", response_model=Tenant)
def create_tenant(tenant: CreateTenant, usecase: TenantUseCase = Depends(get_usecase)):
    return usecase.create_tenant(tenant)

@router.patch("/{id}", response_model=Tenant)
def update_tenant(id: int, tenant: UpdateTenant, usecase: TenantUseCase = Depends(get_usecase)):
    return usecase.update_tenant(id, tenant)

@router.delete("/{id}", response_model=Tenant)
def delete_tenant(id: int, usecase: TenantUseCase = Depends(get_usecase)):
    return usecase.delete_tenant(id)
