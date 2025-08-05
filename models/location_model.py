from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base
from sqlalchemy.orm import relationship

class Location(Base):
    __tablename__ = "locations"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    address = Column(String, index=True)
    city = Column(String, index=True)
    state = Column(String, index=True)
    country = Column(String, index=True)
    postal_code = Column(String, index=True)
    latitude = Column(String)
    longitude = Column(String)
    property_id = Column(Integer, ForeignKey("properties.id"))

    property = relationship("Property", back_populates="location")