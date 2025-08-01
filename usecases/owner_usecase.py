from fastapi import HTTPException
from services.owner_service import OwnerService
from schemas.owner_schema import CreateOwner, GetOwnersDto, UpdateOwner

class OwnerUseCase:
    def __init__(self):
        self.service = OwnerService()

    def get_owners(self, queries: GetOwnersDto):
        return self.service.get_owners(queries)

    def get_owner_by_id(self, id: int):
        data = self.service.get_owner(id)
        if not data:
            raise HTTPException(status_code=400, detail="owner not found")
        return data

    def create_owner(self, data: CreateOwner):
        return self.service.create_owner(data)

    def update_owner(self, id: int, data: UpdateOwner):
        return self.service.update_owner(id, data)

    def delete_owner(self, id: int):
        return self.service.delete_owner(id)
