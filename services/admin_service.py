from schemas.admin_schema import CreateAdmin, GetAdminsDto, UpdateAdmin
from repositories.admin_repository import AdminRepository
from services.password_service import PasswordService

class AdminService:
    def __init__(self):
        self.repository = AdminRepository()
        self.password_service = PasswordService()

    def get_admins(self, queries: GetAdminsDto):
        return self.repository.get_all(queries)

    def get_admin(self, id: int):
        return self.repository.get_by_id(id)
    
    def get_admin_by_email(self, email: str):
        return self.repository.find_one('email', email)

    def create_admin(self, data: CreateAdmin):
        return self.repository.create(data)

    def update_admin(self, id: int, data: UpdateAdmin):
        return self.repository.update(id, data)

    def delete_admin(self, id: int):
        return self.repository.delete(id)
