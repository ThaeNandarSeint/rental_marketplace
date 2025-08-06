from database import SessionLocal
from models.property_file_model import PropertyFile
from schemas.property_file_schema import CreatePropertyFile, GetPropertyFilesDto, UpdatePropertyFile

class PropertyFileRepository:
    def __init__(self):
        self.db = SessionLocal()

    def get_all(self, queries: GetPropertyFilesDto):
        dbQuery = self.db.query(PropertyFile)

        if queries.search:
            search = f"%{queries.search}%"
            dbQuery = dbQuery.filter(
                (PropertyFile.name.ilike(search))
            )

        data = dbQuery.offset(queries.skip).limit(queries.limit).all()
        count = dbQuery.count()
        return {
            "data": data,
            "count": count
        }

    def get_by_id(self, id: int):
        return self.db.query(PropertyFile).filter(PropertyFile.id == id).first()
    
    def find_one(self, field: str, value):
        model_field = getattr(PropertyFile, field, None)
        if model_field is None:
            raise ValueError(f"Invalid field: {field}")
        
        return self.db.query(PropertyFile).filter(model_field == value).first()

    def create(self, data: CreatePropertyFile):
        db_data = PropertyFile(**data.model_dump())
        self.db.add(db_data)
        self.db.commit()
        self.db.refresh(db_data)
        return db_data

    def update(self, id: int, data: UpdatePropertyFile):
        db_data = self.get_by_id(id)
        if db_data:
            db_data.name = data.name
            self.db.commit()
            self.db.refresh(db_data)
        return db_data

    def delete(self, id: int):
        db_data = self.get_by_id(id)
        if db_data:
            self.db.delete(db_data)
            self.db.commit()
        return db_data
