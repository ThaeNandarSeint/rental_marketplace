from fastapi import HTTPException
from services.tenant_service import TenantService
from schemas.tenant_schema import CreateTenant, GetTenantsDto, UpdateTenant

class TenantUseCase:
    def __init__(self):
        self.service = TenantService()

    def get_tenants(self, queries: GetTenantsDto):
        result = self.service.get_tenants(queries)
        print("-----------------------------------")
        print(result)
        print("-----------------------------------")
        return result

    def get_tenant_by_id(self, id: int):
        data = self.service.get_tenant(id)
        if not data:
            raise HTTPException(status_code=400, detail="tenant not found")
        return data

    def create_tenant(self, data: CreateTenant):
        return self.service.create_tenant(data)

    def update_tenant(self, id: int, data: UpdateTenant):
        return self.service.update_tenant(id, data)

    def delete_tenant(self, id: int):
        return self.service.delete_tenant(id)
