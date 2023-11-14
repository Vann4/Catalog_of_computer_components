from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/goods/", response_model=list[schemas.Goods])
def get_goods(db: Session = Depends(get_db)):
    goods = crud.get_goods(db)
    return goods


@app.post("/good/", response_model=schemas.Goods)
def create_good(good: schemas.GoodsCreate, db: Session = Depends(get_db)):
    return crud.create_good(good=good, db=db)


@app.get("/product_characteristic/", response_model=list[schemas.ProductCharacteristic])
def get_product_characteristic(db: Session = Depends(get_db)):
    product_characteristic = crud.get_product_characteristic(db)
    return product_characteristic


@app.post("/product_characteristic/", response_model=schemas.ProductCharacteristic)
def create_product_characteristic(product_characteristic: schemas.ProductCharacteristicCreate, db: Session = Depends(get_db)):
    return crud.create_product_characteristic(db=db, product_characteristic=product_characteristic)


@app.get("/category/", response_model=list[schemas.Category])
def get_category(db: Session = Depends(get_db)):
    category = crud.get_category(db)
    return category


# @app.post("/category/", response_model=schemas.Category)
# def create_owner(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
#     db_category = crud.get_category_by_appellation(db, appellation=category.appellation)
#     if db_category:
#         raise HTTPException(status_code=400, detail="Такая категория уже существует")
#     return crud.create_category(db=db, category=category)


@app.get("/owners/", response_model=list[schemas.Owner])
def get_owners(db: Session = Depends(get_db)):
    owners = crud.get_owners(db)
    return owners


@app.post("/owner/", response_model=schemas.Owner)
def create_owner(owner: schemas.OwnerCreate, db: Session = Depends(get_db)):
    db_owner = crud.get_owner_by_email(db, email=owner.email)
    if db_owner:
        raise HTTPException(status_code=400, detail="Человек с такой почтой уже зарегистрирован")
    return crud.create_owner(db=db, owner=owner)
