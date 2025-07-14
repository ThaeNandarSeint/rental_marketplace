from services.user_service import UserService
from schemas.user_schema import UserCreate, UserUpdate

class UserUseCase:
    def __init__(self, service: UserService):
        self.service = service

    def list_users(self):
        return self.service.get_users()

    def retrieve_user(self, user_id: int):
        return self.service.get_user(user_id)

    def add_user(self, user: UserCreate):
        return self.service.create_user(user)

    def modify_user(self, user_id: int, user: UserUpdate):
        return self.service.update_user(user_id, user)

    def remove_user(self, user_id: int):
        return self.service.delete_user(user_id)
