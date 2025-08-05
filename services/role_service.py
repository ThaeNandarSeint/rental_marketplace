from fastapi import HTTPException
from schemas.role_schema import CreateRole, GetRolesDto, UpdateRole
from repositories.role_repository import RoleRepository
from services.password_service import PasswordService

class RoleService:
    def __init__(self):
        self.repository = RoleRepository()
        self.password_service = PasswordService()

    def get_roles(self, queries: GetRolesDto):
        return self.repository.get_all(queries)

    def get_role(self, id: int):
        return self.repository.get_by_id(id)
    
    def get_role_by_name(self, name: str):
        return self.repository.find_one('name', name)

    def create_role(self, data: CreateRole):
        old_role = self.get_role_by_name(data.name)
        if old_role:
            raise HTTPException(status_code=400, detail="This name already registered.")

        return self.repository.create(data)

    def update_role(self, id: int, data: UpdateRole):
        return self.repository.update(id, data)

    def delete_role(self, id: int):
        return self.repository.delete(id)
