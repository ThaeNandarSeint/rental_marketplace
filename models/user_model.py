from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship
from database import Base
import enum

class UserType(enum.Enum):
    ADMIN = "admin"
    OWNER = "owner"
    TENANT = "tenant"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    phone_number = Column(String, index=True)
    type = Column(String, nullable=False)

    tenant = relationship("Tenant", back_populates="user", uselist=False)
    owner = relationship("Owner", back_populates="user", uselist=False)
    admin = relationship("Admin", back_populates="user", uselist=False)