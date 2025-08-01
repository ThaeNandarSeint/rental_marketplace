from database import SessionLocal
from sqlalchemy.orm import joinedload
from models.tenant_model import Tenant
from schemas.tenant_schema import CreateTenant, GetTenantsDto, UpdateTenant

class TenantRepository:
    def __init__(self):
        self.db = SessionLocal()

    def get_all(self, queries: GetTenantsDto):
        dbQuery = self.db.query(Tenant).options(joinedload(Tenant.user))

        # search = f"%{queries.search}%"
        # dbQuery = dbQuery.filter(
        #     (Tenant.name.ilike(search)) | (Tenant.email.ilike(search))
        # )

        data = dbQuery.offset(queries.skip).limit(queries.limit).all()
        count = dbQuery.count()

        return {
            "data": data,
            "count": count
        }

    def get_by_id(self, id: int):
        return self.db.query(Tenant).filter(Tenant.id == id).first()
    
    def find_one(self, field: str, value):
        model_field = getattr(Tenant, field, None)
        if model_field is None:
            raise ValueError(f"Invalid field: {field}")
        
        return self.db.query(Tenant).filter(model_field == value).first()

    def create(self, data: CreateTenant):
        db_data = Tenant(**data)
        self.db.add(db_data)
        self.db.commit()
        self.db.refresh(db_data)
        return db_data

    def update(self, id: int, data: UpdateTenant):
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
