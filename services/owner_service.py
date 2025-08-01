from schemas.owner_schema import CreateOwner, GetOwnersDto, UpdateOwner
from repositories.owner_repository import OwnerRepository
from services.password_service import PasswordService

class OwnerService:
    def __init__(self):
        self.repository = OwnerRepository()
        self.password_service = PasswordService()

    def get_owners(self, queries: GetOwnersDto):
        return self.repository.get_all(queries)

    def get_owner(self, id: int):
        return self.repository.get_by_id(id)
    
    def get_owner_by_email(self, email: str):
        return self.repository.find_one('email', email)

    def create_owner(self, data: CreateOwner):
        return self.repository.create(data)

    def update_owner(self, id: int, data: UpdateOwner):
        return self.repository.update(id, data)

    def delete_owner(self, id: int):
        return self.repository.delete(id)
