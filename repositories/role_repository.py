from database import SessionLocal
from models.role_model import Role
from schemas.role_schema import CreateRole, GetRolesDto, UpdateRole

class RoleRepository:
    def __init__(self):
        self.db = SessionLocal()

    def get_all(self, queries: GetRolesDto):
        dbQuery = self.db.query(Role)

        if queries.search:
            search = f"%{queries.search}%"
            dbQuery = dbQuery.filter(
                (Role.name.ilike(search)) | (Role.email.ilike(search))
            )

        data = dbQuery.offset(queries.skip).limit(queries.limit).all()
        count = dbQuery.count()
        return {
            "data": data,
            "count": count
        }

    def get_by_id(self, role_id: int):
        return self.db.query(Role).filter(Role.id == role_id).first()
    
    def find_one(self, field: str, value):
        model_field = getattr(Role, field, None)
        if model_field is None:
            raise ValueError(f"Invalid field: {field}")
        
        return self.db.query(Role).filter(model_field == value).first()

    def create(self, data: CreateRole):
        db_data = Role(**data.model_dump())
        self.db.add(db_data)
        self.db.commit()
        self.db.refresh(db_data)
        return db_data

    def update(self, role_id: int, Role: UpdateRole):
        db_role = self.get_by_id(role_id)
        if db_role:
            db_role.name = Role.name
            db_role.email = Role.email
            self.db.commit()
            self.db.refresh(db_role)
        return db_role

    def delete(self, role_id: int):
        db_role = self.get_by_id(role_id)
        if db_role:
            self.db.delete(db_role)
            self.db.commit()
        return db_role
