from database import SessionLocal
from sqlalchemy.orm import joinedload
from models.owner_model import Owner
from schemas.owner_schema import CreateOwner, GetOwnersDto, UpdateOwner

class OwnerRepository:
    def __init__(self):
        self.db = SessionLocal()

    def get_all(self, queries: GetOwnersDto):
        dbQuery = self.db.query(Owner).options(joinedload(Owner.user))

        # search = f"%{queries.search}%"
        # dbQuery = dbQuery.filter(
        #     (Owner.name.ilike(search)) | (Owner.email.ilike(search))
        # )

        data = dbQuery.offset(queries.skip).limit(queries.limit).all()
        count = dbQuery.count()
        return {
            "data": data,
            "count": count
        }

    def get_by_id(self, id: int):
        return self.db.query(Owner).filter(Owner.id == id).first()
    
    def find_one(self, field: str, value):
        model_field = getattr(Owner, field, None)
        if model_field is None:
            raise ValueError(f"Invalid field: {field}")
        
        return self.db.query(Owner).filter(model_field == value).first()

    def create(self, data: CreateOwner):
        db_data = Owner(**data)
        self.db.add(db_data)
        self.db.commit()
        self.db.refresh(db_data)
        return db_data

    def update(self, id: int, data: UpdateOwner):
        db_data = self.get_by_id(id)
        if db_data:
            db_data.name = data.name
            db_data.email = data.email
            self.db.commit()
            self.db.refresh(db_data)
        return db_data

    def delete(self, id: int):
        db_data = self.get_by_id(id)
        if db_data:
            self.db.delete(db_data)
            self.db.commit()
        return db_data
