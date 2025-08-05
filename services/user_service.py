from fastapi import HTTPException
from schemas.user_schema import CreateUser, GetUsersDto, UpdateUser
from repositories.user_repository import UserRepository
from services.password_service import PasswordService

class UserService:
    def __init__(self):
        self.repository = UserRepository()
        self.password_service = PasswordService()

    def get_users(self, queries: GetUsersDto):
        return self.repository.get_all(queries)

    def get_user(self, id: int):
        return self.repository.get_by_id(id)
    
    def get_user_by_email(self, email: str):
        return self.repository.find_one('email', email)

    def create_user(self, data: CreateUser):
        old_user = self.get_user_by_email(data.email)
        if old_user:
            raise HTTPException(status_code=400, detail="Email already registered.")
        
        user_data = data.model_dump()
        user_data["password"] = self.password_service.hash(data.password)
        return self.repository.create(user_data)

    def update_user(self, id: int, data: UpdateUser):
        return self.repository.update(id, data)

    def delete_user(self, id: int):
        return self.repository.delete(id)
