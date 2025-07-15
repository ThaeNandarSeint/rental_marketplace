from services.user_service import UserService
from schemas.user_schema import UserCreate, UserUpdate

class UserUseCase:
    def __init__(self, service: UserService):
        self.service = service

    def get_users(self):
        return self.service.get_users()

    def get_user_by_id(self, user_id: int):
        return self.service.get_user(user_id)

    def create_user(self, user: UserCreate):
        return self.service.create_user(user)

    def update_user(self, user_id: int, user: UserUpdate):
        return self.service.update_user(user_id, user)

    def delete_user(self, user_id: int):
        return self.service.delete_user(user_id)
