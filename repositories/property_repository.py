from database import SessionLocal
from models.property_model import Property
from schemas.property_schema import CreateProperty, GetPropertiesDto, UpdateProperty

class PropertyRepository:
    def __init__(self):
        self.db = SessionLocal()

    def get_all(self, queries: GetPropertiesDto):
        dbQuery = self.db.query(Property)

        if queries.search:
            search = f"%{queries.search}%"
            dbQuery = dbQuery.filter(
                (Property.name.ilike(search))
            )

        data = dbQuery.offset(queries.skip).limit(queries.limit).all()
        count = dbQuery.count()
        return {
            "data": data,
            "count": count
        }

    def get_by_id(self, id: int):
        return self.db.query(Property).filter(Property.id == id).first()
    
    def find_one(self, field: str, value):
        model_field = getattr(Property, field, None)
        if model_field is None:
            raise ValueError(f"Invalid field: {field}")
        
        return self.db.query(Property).filter(model_field == value).first()

    def create(self, data: CreateProperty):
        db_data = Property(**data.model_dump())
        self.db.add(db_data)
        self.db.commit()
        self.db.refresh(db_data)
        return db_data

    def update(self, id: int, data: UpdateProperty):
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
