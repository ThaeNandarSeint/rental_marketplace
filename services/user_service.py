from schemas.user_schema import UserCreate, UserUpdate
from repositories.user_repository import UserRepository

class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def get_users(self):
        return self.repository.get_all()

    def get_user(self, user_id: int):
        return self.repository.get_by_id(user_id)

    def create_user(self, user: UserCreate):
        return self.repository.create(user)

    def update_user(self, user_id: int, user: UserUpdate):
        return self.repository.update(user_id, user)

    def delete_user(self, user_id: int):
        return self.repository.delete(user_id)
