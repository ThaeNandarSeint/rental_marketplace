from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base
from sqlalchemy.orm import relationship

class PropertyFile(Base):
    __tablename__ = "property_files"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True)
    url = Column(String)
    type = Column(String)
    property_id = Column(Integer, ForeignKey('properties.id'))

    property = relationship("Property", back_populates="files")