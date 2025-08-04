from database import SessionLocal
from models.category_model import Category
from schemas.category_schema import CreateCategory, GetCategoriesDto, UpdateCategory

class CategoryRepository:
    def __init__(self):
        self.db = SessionLocal()

    def get_all(self, queries: GetCategoriesDto):
        dbQuery = self.db.query(Category)

        if queries.search:
            search = f"%{queries.search}%"
            dbQuery = dbQuery.filter(
                (Category.name.ilike(search)) | (Category.email.ilike(search))
            )

        data = dbQuery.offset(queries.skip).limit(queries.limit).all()
        count = dbQuery.count()
        return {
            "data": data,
            "count": count
        }

    def get_by_id(self, id: int):
        return self.db.query(Category).filter(Category.id == id).first()
    
    def find_one(self, field: str, value):
        model_field = getattr(Category, field, None)
        if model_field is None:
            raise ValueError(f"Invalid field: {field}")
        
        return self.db.query(Category).filter(model_field == value).first()

    def create(self, data: CreateCategory):
        db_data = Category(**data.model_dump())
        self.db.add(db_data)
        self.db.commit()
        self.db.refresh(db_data)
        return db_data

    def update(self, id: int, data: UpdateCategory):
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
