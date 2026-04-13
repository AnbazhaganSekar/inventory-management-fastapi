from sqlalchemy import Column, Integer, String, Float
from .database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String(255))
    category = Column(String(100))
    quantity = Column(Integer)
    price = Column(Float)