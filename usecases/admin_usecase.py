from fastapi import HTTPException
from services.admin_service import AdminService
from schemas.admin_schema import CreateAdmin, GetAdminsDto, UpdateAdmin
from services.user_service import UserService

class AdminUseCase:
    def __init__(self):
        self.service = AdminService()
        self.user_service = UserService()

    def get_admins(self, queries: GetAdminsDto):
        return self.service.get_admins(queries)

    def get_admin_by_id(self, id: int):
        data = self.service.get_admin(id)
        if not data:
            raise HTTPException(status_code=400, detail="Admin not found")
        return data

    def create_admin(self, data: CreateAdmin):
        data.user.type = 'admin'
        user = self.user_service.create_user(data.user)
        return self.service.create_admin({'user_id': user.id, 'role_id': data.role_id})

    def update_admin(self, id: int, data: UpdateAdmin):
        return self.service.update_admin(id, data)

    def delete_admin(self, id: int):
        return self.service.delete_admin(id)
