from fastapi import HTTPException
from services.user_service import UserService
from schemas.user_schema import CreateUser, GetUsersDto, UpdateUser

class UserUseCase:
    def __init__(self):
        self.service = UserService()

    def get_users(self, queries: GetUsersDto):
        return self.service.get_users(queries)

    def get_user_by_id(self, id: int):
        data = self.service.get_user(id)
        if not data:
            raise HTTPException(status_code=400, detail="User not found")
        return data

    def create_user(self, data: CreateUser):
        return self.service.create_user(data)

    def update_user(self, id: int, data: UpdateUser):
        return self.service.update_user(id, data)

    def delete_user(self, id: int):
        return self.service.delete_user(id)
