from fastapi import FastAPI, Request, Form, Depends
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session

from .database import SessionLocal, engine, Base
from . import crud

app = FastAPI()

Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home(request: Request, db: Session = Depends(get_db)):
    products = crud.get_products(db)
    return templates.TemplateResponse("index.html", {
        "request": request,
        "products": products
    })

@app.post("/add")
def add_product(
    product_name: str = Form(...),
    category: str = Form(...),
    quantity: int = Form(...),
    price: float = Form(...),
    db: Session = Depends(get_db)
):
    crud.add_product(db, {
        "product_name": product_name,
        "category": category,
        "quantity": quantity,
        "price": price
    })
    return {"message": "Product Added"}

@app.get("/delete/{id}")
def delete_product(id: int, db: Session = Depends(get_db)):
    crud.delete_product(db, id)
    return {"message": "Deleted"}