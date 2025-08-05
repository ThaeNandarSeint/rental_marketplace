from sqlalchemy import Column, Integer, String
from database import Base
from sqlalchemy.orm import relationship

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True)

    properties = relationship("Property", back_populates="category")