from sqlalchemy.orm import Session
from .models import Product

def get_products(db: Session):
    return db.query(Product).all()

def add_product(db: Session, data):
    product = Product(**data)
    db.add(product)
    db.commit()

def delete_product(db: Session, product_id):
    product = db.query(Product).filter(Product.id == product_id).first()
    if product:
        db.delete(product)
        db.commit()