from fastapi import HTTPException
from services.role_service import RoleService
from schemas.role_schema import CreateRole, GetRolesDto, UpdateRole

class RoleUseCase:
    def __init__(self):
        self.service = RoleService()

    def get_roles(self, queries: GetRolesDto):
        return self.service.get_roles(queries)

    def get_role_by_id(self, id: int):
        data = self.service.get_role(id)
        if not data:
            raise HTTPException(status_code=400, detail="Role not found")
        return data

    def create_role(self, data: CreateRole):
        return self.service.create_role(data)

    def update_role(self, id: int, data: UpdateRole):
        return self.service.update_role(id, data)

    def delete_role(self, id: int):
        return self.service.delete_role(id)
