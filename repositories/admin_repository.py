from database import SessionLocal
from sqlalchemy.orm import joinedload
from models.admin_model import Admin
from schemas.admin_schema import CreateAdmin, GetAdminsDto, UpdateAdmin

class AdminRepository:
    def __init__(self):
        self.db = SessionLocal()

    def get_all(self, queries: GetAdminsDto):
        dbQuery = self.db.query(Admin).options(joinedload(Admin.user))

        # search = f"%{queries.search}%"
        # dbQuery = dbQuery.filter(
        #     (admin.name.ilike(search)) | (admin.email.ilike(search))
        # )

        data = dbQuery.offset(queries.skip).limit(queries.limit).all()
        count = dbQuery.count()

        return {
            "data": data,
            "count": count
        }

    def get_by_id(self, id: int):
        return self.db.query(Admin).filter(Admin.id == id).first()
    
    def find_one(self, field: str, value):
        model_field = getattr(Admin, field, None)
        if model_field is None:
            raise ValueError(f"Invalid field: {field}")
        
        return self.db.query(Admin).filter(model_field == value).first()

    def create(self, data: CreateAdmin):
        db_data = Admin(**data)
        self.db.add(db_data)
        self.db.commit()
        self.db.refresh(db_data)
        return db_data

    def update(self, id: int, data: UpdateAdmin):
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
