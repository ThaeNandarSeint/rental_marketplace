from sqlalchemy import Column, Integer, ForeignKey
from database import Base
from sqlalchemy.orm import relationship

class FavouriteProperty(Base):
    __tablename__ = "favourite_properties"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    tenant_id = Column(Integer, ForeignKey('tenants.id'))
    property_id = Column(Integer, ForeignKey('properties.id'))

    tenant = relationship("Tenant", back_populates="favourite_properties")
    property = relationship("Property", back_populates="favourite_properties")