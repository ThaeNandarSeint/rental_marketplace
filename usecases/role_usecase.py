from fastapi import HTTPException
from services.role_service import RoleService
from schemas.role_schema import CreateRole, GetRolesDto, UpdateRole

class RoleUseCase:
    def __init__(self):
        self.service = RoleService()

    def get_roles(self, queries: GetRolesDto):
        return self.service.get_roles(queries)

    def get_role_by_id(self, role_id: int):
        data = self.service.get_role(role_id)
        if not data:
            raise HTTPException(status_code=400, detail="Role not found")
        return data

    def create_role(self, Role: CreateRole):
        return self.service.create_role(Role)

    def update_role(self, role_id: int, Role: UpdateRole):
        return self.service.update_role(role_id, Role)

    def delete_role(self, role_id: int):
        return self.service.delete_role(role_id)
