from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from database import Base

class Admin(Base):
    __tablename__ = "admins"

    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)

    # user = relationship("User", back_populates="admin")