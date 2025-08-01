from schemas.tenant_schema import CreateTenant, GetTenantsDto, UpdateTenant
from repositories.tenant_repository import TenantRepository
from services.password_service import PasswordService

class TenantService:
    def __init__(self):
        self.repository = TenantRepository()
        self.password_service = PasswordService()

    def get_tenants(self, queries: GetTenantsDto):
        return self.repository.get_all(queries)

    def get_tenant(self, id: int):
        return self.repository.get_by_id(id)
    
    def get_tenant_by_email(self, email: str):
        return self.repository.find_one('email', email)

    def create_tenant(self, data: CreateTenant):
        return self.repository.create(data)

    def update_tenant(self, id: int, data: UpdateTenant):
        return self.repository.update(id, data)

    def delete_tenant(self, id: int):
        return self.repository.delete(id)
