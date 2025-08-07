from sqlalchemy import Column, Integer, String, Date, ForeignKey
from database import Base
from sqlalchemy.orm import relationship

class Property(Base):
    __tablename__ = "properties"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, index=True)
    description = Column(String)
    min_price_per_day = Column(Integer, nullable=True)
    max_price_per_day = Column(Integer, nullable=True)
    min_price_per_month = Column(Integer)
    max_price_per_month = Column(Integer)
    deposit = Column(Integer)
    electric_price = Column(Integer)
    water_price = Column(Integer)
    service_fee = Column(Integer)
    internet_bill = Column(Integer)
    category_id = Column(Integer, ForeignKey('categories.id'))
    owner_id = Column(Integer, ForeignKey('owners.id'))

    category = relationship("Category", back_populates="properties")
    owner = relationship("Owner", back_populates="properties")
    location = relationship("Location", back_populates="property", uselist=False)
    files = relationship("PropertyFile", back_populates="property")
    favourite_properties = relationship("FavouriteProperty", back_populates="property")