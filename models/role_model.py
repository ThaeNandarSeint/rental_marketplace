from sqlalchemy import Column, Integer, String
from database import Base
from sqlalchemy.orm import relationship

class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True)

    admins = relationship("Admin", back_populates="role")