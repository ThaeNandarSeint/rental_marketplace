from database import SessionLocal
from models.user_model import User
from schemas.user_schema import CreateUser, GetUsersDto, UpdateUser

class UserRepository:
    def __init__(self):
        self.db = SessionLocal()

    def get_all(self, queries: GetUsersDto):
        dbQuery = self.db.query(User)

        search = f"%{queries.search}%"
        dbQuery = dbQuery.filter(
            (User.name.ilike(search)) | (User.email.ilike(search))
        )

        data = dbQuery.offset(queries.skip).limit(queries.limit).all()
        count = dbQuery.count()
        return {
            "data": data,
            "count": count
        }

    def get_by_id(self, user_id: int):
        return self.db.query(User).filter(User.id == user_id).first()
    
    def find_one(self, field: str, value):
        model_field = getattr(User, field, None)
        if model_field is None:
            raise ValueError(f"Invalid field: {field}")
        
        return self.db.query(User).filter(model_field == value).first()

    def create(self, user: CreateUser):
        db_user = User(**user)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def update(self, user_id: int, user: UpdateUser):
        db_user = self.get_by_id(user_id)
        if db_user:
            db_user.name = user.name
            db_user.email = user.email
            self.db.commit()
            self.db.refresh(db_user)
        return db_user

    def delete(self, user_id: int):
        db_user = self.get_by_id(user_id)
        if db_user:
            self.db.delete(db_user)
            self.db.commit()
        return db_user
