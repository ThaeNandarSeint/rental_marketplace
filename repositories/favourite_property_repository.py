from database import SessionLocal
from sqlalchemy.orm import joinedload
from models.favourite_property_model import FavouriteProperty
from schemas.favourite_property_schema import CreateFavouriteProperty, GetFavouritePropertiesDto, UpdateFavouriteProperty

class FavouritePropertyRepository:
    def __init__(self):
        self.db = SessionLocal()

    def get_all(self, queries: GetFavouritePropertiesDto):
        dbQuery = self.db.query(FavouriteProperty).options(joinedload(FavouriteProperty.tenant), joinedload(FavouriteProperty.property))

        data = dbQuery.offset(queries.skip).limit(queries.limit).all()
        count = dbQuery.count()
        return {
            "data": data,
            "count": count
        }

    def get_by_id(self, id: int):
        return self.db.query(FavouriteProperty).filter(FavouriteProperty.id == id).first()
    
    def find_one(self, field: str, value):
        model_field = getattr(FavouriteProperty, field, None)
        if model_field is None:
            raise ValueError(f"Invalid field: {field}")
        
        return self.db.query(FavouriteProperty).filter(model_field == value).first()

    def create(self, data: CreateFavouriteProperty):
        db_data = FavouriteProperty(**data.model_dump())
        self.db.add(db_data)
        self.db.commit()
        self.db.refresh(db_data)
        return db_data

    def update(self, id: int, data: UpdateFavouriteProperty):
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
